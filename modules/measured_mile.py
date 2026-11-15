import streamlit as st
import pandas as pd

from utils.validation import validate_columns

from calculations.calc_measured_mile import (
    calculate_productivity,
    calculate_kpis
)

from visualizations.visual_measured_mile import (
    productivity_chart
)


def show_measured_mile():

    st.title("Measured Mile")

    st.markdown("""
    ## Overview

    The Measured Mile methodology compares productivity achieved
    during an impacted period against productivity achieved
    during a representative unimpacted period.

    **Core Formula**

    Productivity = Quantity Installed / Labour Hours
    """)

    with st.expander("Expected Dataset Structure"):

        st.markdown("""
        Required Columns:

        - Period
        - Type
        - Quantity
        - LabourHours

        Type Values:

        - MeasuredMile
        - Impacted
        """)

    st.markdown("---")

    uploaded_file = st.file_uploader(
        "Upload CSV or Excel File",
        type=["csv", "xlsx"]
    )

    if uploaded_file is None:
        return

    try:

        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)

        else:
            df = pd.read_excel(uploaded_file)

    except Exception as e:

        st.error(
            f"Error reading file: {e}"
        )

        return

    required_columns = [
        "Period",
        "Type",
        "Quantity",
        "LabourHours"
    ]

    missing_columns = validate_columns(
        df,
        required_columns
    )

    if missing_columns:

        st.error(
            "Missing required columns: "
            + ", ".join(missing_columns)
        )

        return

    st.success(
        "Dataset structure validated successfully."
    )

    st.subheader("Input Data")

    st.dataframe(
        df,
        use_container_width=True
    )

    df = calculate_productivity(df)

    st.subheader("Calculated Productivity")

    st.dataframe(
        df,
        use_container_width=True
    )

    kpis = calculate_kpis(df)

    st.markdown("---")

    st.header("Results")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Measured Mile Productivity",
            f"{kpis['mm_productivity']:.2f}"
        )

    with col2:

        st.metric(
            "Impacted Productivity",
            f"{kpis['impacted_productivity']:.2f}"
        )

    with col3:

        st.metric(
            "Productivity Loss %",
            f"{kpis['productivity_loss']:.1f}%"
        )

    st.markdown("---")

    st.header("Productivity Trend")

    fig = productivity_chart(df)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")

    st.header("Interpretation")

    st.info(
        "Narrative Engine to be added in a future release."
    )