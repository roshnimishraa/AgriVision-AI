import os
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image

from src import model_loader, disease_detection, yield_prediction, config, yield_explainability, report_generator
from src.ui import theme


def render():

    theme.hero()

    if not model_loader.encoders_available() or not model_loader.endtoend_model_available():
        st.warning("This tool isn't available right now — please check back later.")
        return

    with st.spinner("Loading the tool..."):
        encoders = model_loader.load_encoders()
        disease_ready = model_loader.disease_model_available()
        sample_available = disease_ready and os.path.exists(config.SAMPLE_LEAF_PATH)

    theme.step_indicator()
    
    has_photo = st.checkbox(
        "I have a leaf photo to check for disease", value=disease_ready,
        disabled=not disease_ready, key="has_photo",
        help=None if disease_ready else "Disease detection isn't available right now.",
    )

    if sample_available and has_photo and not st.session_state.get("using_sample"):
        if st.button("Try a sample photo instead", key="sample_btn"):
            st.session_state["using_sample"] = True
            st.rerun()

    with st.form("main_form"):
        uploaded = None

        if has_photo:
            if st.session_state.get("using_sample"):
                st.image(config.SAMPLE_LEAF_PATH, caption="Sample photo (loaded)", width=200)

                remove_sample = st.form_submit_button("Use my own photo instead")

                if remove_sample:
                    st.session_state["using_sample"] = False
                    st.rerun()

            else:
                uploaded = st.file_uploader(
                    "Upload a leaf photo",
                    type=["jpg", "jpeg", "png"],
                    key="main_upload"
                )

        st.markdown("#### Field conditions")

        c1, c2, c3 = st.columns(3)

        with c1:
            area = st.selectbox(
                "Region",
                sorted(encoders["area_encoder"].classes_),
                index=None,
                placeholder="Select a region",
                key="area",
            )

            year = st.number_input(
                "Year",
                min_value=1990,
                max_value=2030,
                value=None,
                placeholder="e.g. 2024",
                key="year",
            )

        with c2:
            if has_photo:
                crop_options = yield_prediction.supported_yield_items(
                    encoders["item_encoder"].classes_
                )

                if not crop_options:
                    crop_options = sorted(encoders["item_encoder"].classes_)

            else:
                crop_options = sorted(encoders["item_encoder"].classes_)

            item = st.selectbox(
                "Crop",
                crop_options,
                index=None,
                placeholder="Select a crop",
                key="item",
            )

            rainfall = st.number_input(
                "Average rainfall (mm/year)",
                min_value=0.0,
                value=None,
                placeholder="e.g. 1200",
                key="rain",
            )

        with c3:
            pesticides = st.number_input(
                "Pesticide use (tonnes)",
                min_value=0.0,
                value=None,
                placeholder="e.g. 100",
                key="pest",
            )

            temp = st.number_input(
                "Average temperature (°C)",
                min_value=-10.0,
                max_value=50.0,
                value=None,
                placeholder="e.g. 25",
                key="temp",
            )

        manual_severity = None

        if not has_photo:
            manual_severity = st.slider(
                "Disease severity (if known)",
                0.0,
                1.0,
                0.0,
                0.05,
                help="Leave at 0 if the crop is healthy or you don't know.",
                key="manual_severity",
            )

        submitted = st.form_submit_button(
            "Analyze" if has_photo else "Estimate Yield",
            type="primary"
        )

    st.markdown("<div style='margin-top:20px;'></div>", unsafe_allow_html=True)

    using_sample = st.session_state.get("using_sample", False)

    image_ready = uploaded is not None or using_sample

    fields_filled = all(
        v is not None
        for v in [area, item, year, rainfall, pesticides, temp]
    )

    if submitted and has_photo and not image_ready:
        st.info(
            "Upload a photo, or uncheck “I have a leaf photo” to estimate yield only."
        )

    elif submitted and not fields_filled:
        st.info(
            "Please fill in all the field conditions before running the analysis."
        )

    elif submitted:

        image_for_analysis = (
            Image.open(config.SAMPLE_LEAF_PATH)
            if using_sample
            else (Image.open(uploaded) if uploaded is not None else None)
        )

        _run_analysis(
            encoders,
            has_photo=has_photo,
            uploaded_image=image_for_analysis,
            area=area,
            item=item,
            year=year,
            rainfall=rainfall,
            pesticides=pesticides,
            temp=temp,
            manual_severity=manual_severity,
        )

    cached = st.session_state.get("analysis")

    if not cached:
        return

    _render_results(cached)
    _render_model_validation()
    
def _current_step():

    if not st.session_state.get("analysis"):
        return 1

    if st.session_state.get("report_ready"):
        return 4

    return 3


def _run_analysis(
    encoders,
    has_photo,
    uploaded_image,
    area,
    item,
    year,
    rainfall,
    pesticides,
    temp,
    manual_severity,
):

    st.session_state["report_ready"] = False

    with st.spinner("Running the analysis..."):

        result, overlay, heatmap_status, pil_img = None, None, None, None

        if has_photo and uploaded_image is not None:

            disease_model = model_loader.load_disease_model()
            disease_meta = model_loader.load_disease_meta()

            pil_img = uploaded_image

            result, overlay, heatmap_status = disease_detection.predict(
                disease_model,
                disease_meta,
                pil_img,
                with_gradcam=True
            )

            severity = result["severity"]

        else:
            severity = manual_severity


        endtoend_model = model_loader.load_endtoend_yield_model()

        fused_pred, fused_row, fused_cols = yield_prediction.predict_with_row(
            endtoend_model,
            encoders,
            area,
            item,
            year,
            rainfall,
            pesticides,
            temp,
            severity=severity,
            severity_feature_name=config.SEVERITY_FEATURE_ENDTOEND,
        )


        baseline_pred = None

        if model_loader.baseline_model_available():

            baseline_model = model_loader.load_baseline_yield_model()

            baseline_pred = yield_prediction.predict(
                baseline_model,
                encoders,
                area,
                item,
                year,
                rainfall,
                pesticides,
                temp,
                severity=None,
                severity_feature_name=None,
            )


        oracle_pred = None

        if (
            has_photo
            and result is not None
            and model_loader.oracle_model_available()
        ):

            oracle_model = model_loader.load_oracle_yield_model()

            oracle_pred = yield_prediction.predict(
                oracle_model,
                encoders,
                area,
                item,
                year,
                rainfall,
                pesticides,
                temp,
                severity=severity,
                severity_feature_name=config.SEVERITY_FEATURE_ORACLE,
            )


        expected_item = None

        if has_photo and result is not None:

            expected_item = yield_prediction.yield_item_for_disease_class(
                result["class"],
                encoders["item_encoder"].classes_
            )


    st.session_state["analysis"] = {
        "has_photo": has_photo and result is not None,
        "image": pil_img,
        "overlay": overlay,
        "heatmap_status": heatmap_status,
        "result": result,
        "fused_pred": fused_pred,
        "fused_row": fused_row,
        "fused_cols": fused_cols,
        "baseline_pred": baseline_pred,
        "oracle_pred": oracle_pred,
        "selected_item": item,
        "expected_item": expected_item,
    }


def _render_results(cached):

    if cached["has_photo"]:

        col_left, col_right = st.columns(2, gap="large")

        with col_left:
            _render_detection(cached)
            _render_download_button(cached)

        with col_right:
            _render_yield(cached)

    else:

        _render_yield(cached)
        _render_download_button(cached)



def _render_download_button(cached):

    try:

        pdf_bytes = report_generator.build_report(cached)

        st.session_state["report_ready"] = True

        st.download_button(
            "Download PDF report",
            data=pdf_bytes,
            file_name="agrivision_report.pdf",
            mime="application/pdf",
        )

    except Exception:

        st.session_state["report_ready"] = False



def _render_detection(cached):

    st.markdown("#### Crop Disease Detection")

    st.markdown(
        '<div class="avi-detection-img">',
        unsafe_allow_html=True
    )


    if cached.get("heatmap_status") == "ok":

        st.image(
            cached["overlay"],
            caption="Grad-CAM: what the AI focused on",
            use_container_width=True
        )

    else:

        st.image(
            cached["image"],
            caption="Your photo",
            use_container_width=True
        )


    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


    result = cached["result"]

    level, label = disease_detection.severity_level(
        result["severity"]
    )


    theme.severity_card(
        "Detected condition",
        result["class"].replace("_", " "),
        f"Severity: {label} ({result['severity']:.2f})  •  {result['confidence']*100:.0f}% confident",
        level,
    )


    if (
        cached["expected_item"]
        and cached["expected_item"] != cached["selected_item"]
    ):

        st.warning(
            f"The photo looks like **{result['class'].split('_')[0]}**, "
            f"but the yield forecast is set to **{cached['selected_item']}**. "
            f"Select **{cached['expected_item']}** as the crop and re-run "
            f"for a meaningful combined result."
        )



def _render_yield(cached):

    st.markdown("#### Yield Forecast")

    st.metric(
        "Yield forecast",
        f"{cached['fused_pred']:,.0f} hg/ha"
    )


    if cached["baseline_pred"] is not None:

        delta = cached["fused_pred"] - cached["baseline_pred"]

        st.metric(
            "Yield if disease ignored",
            f"{cached['baseline_pred']:,.0f} hg/ha",
            f"{delta:+,.0f} vs disease-aware"
        )


    if cached["oracle_pred"] is not None:

        st.metric(
            "Best-case forecast",
            f"{cached['oracle_pred']:,.0f} hg/ha"
        )


    fig = yield_explainability.explain_prediction(
        cached["fused_row"],
        cached["fused_cols"]
    )


    if fig is not None:

        st.markdown("**Why this forecast (SHAP)**")

        st.pyplot(
            fig,
            use_container_width=True
        )

        plt.close(fig)
        
def _render_model_validation():

    disease_figures = [
        (
            config.DISEASE_CONFUSION_MATRIX_PATH,
            "Confusion Matrix",
            "Shows which disease classes the model confuses most often."
        ),
        (
            config.DISEASE_GRADCAM_SAMPLE_PATH,
            "Grad-CAM Heatmap",
            "Grad-CAM highlights the regions of a leaf image that most influenced the CNN's disease classification."
        ),
        (
            config.DISEASE_OCCLUSION_SALIENCY_PATH,
            "Occlusion Saliency",
            "A second independent method for validating model attention."
        ),
        (
            config.DISEASE_SHAP_FEATURE_IMPORTANCE_PATH,
            "SHAP Explanation (XGBoost)",
            "Feature importance obtained using SHAP for the classical disease classifier."
        ),
    ]


    yield_figures = [
        (
            config.YIELD_SHAP_BAR_PATH,
            "SHAP Feature Importance",
            "Overall importance of each feature for yield prediction."
        ),
        (
            config.YIELD_SHAP_BEESWARM_PATH,
            "SHAP Beeswarm Plot",
            "Distribution of feature impact across all predictions."
        ),
        (
            config.YIELD_SHAP_WATERFALL_PATH,
            "SHAP Waterfall Plot",
            "Explains an individual crop yield prediction."
        ),
        (
            config.YIELD_FUSION_COMPARISON_PATH,
            "Model Comparison",
            "Comparison of Baseline, End-to-End and Oracle models."
        ),
    ]


    disease_available = [
        f for f in disease_figures if os.path.exists(f[0])
    ]

    yield_available = [
        f for f in yield_figures if os.path.exists(f[0])
    ]


    if not disease_available and not yield_available:
        return


    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("## Model Validation")

    st.caption(
        "Performance evaluation and explainability results generated during model training."
    )


    with st.expander("Explore Validation Results", expanded=False):

        st.markdown(
            "<div style='height:20px'></div>",
            unsafe_allow_html=True
        )


        if disease_available and yield_available:

            tab1, tab2 = st.tabs(
                [
                    "Disease Detection",
                    "Yield Prediction"
                ]
            )


            with tab1:
                _render_figure_grid(disease_available)


            with tab2:
                _render_figure_grid(yield_available)


        elif disease_available:

            _render_figure_grid(disease_available)


        else:

            _render_figure_grid(yield_available)



        st.markdown(
            "<div style='height:20px'></div>",
            unsafe_allow_html=True
        )


    st.markdown(
        "<div style='height:40px'></div>",
        unsafe_allow_html=True
    )


def _render_figure_grid(figures):

    for i in range(0, len(figures), 2):

        row = figures[i:i + 2]

        cols = st.columns(
            2,
            gap="large"
        )


        for col, (path, title, caption) in zip(cols, row):

            with col:

                st.markdown(
                    f"""
                    <div class="avi-figure-card">
                        <div class="avi-fig-title">
                            {title}
                        </div> 
                    """,
                    unsafe_allow_html=True,
                )


                st.image(
                    path,
                    use_container_width=True,
                )


                st.markdown(
                    f"""
                        <div class="avi-fig-caption">
                            {caption}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
