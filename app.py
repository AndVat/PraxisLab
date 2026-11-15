import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="PraxisLab",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("PraxisLab")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Measured Mile",
        "Earned Value",
        "Total Unit Cost",
        "Disruption Assistant"
    ]
)

# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------

if page == "Home":

    st.title("PraxisLab")
    st.subheader("Construction Methodologies in Practice")

    st.markdown("---")

    st.markdown("""
    ## Vision

    PraxisLab is a professional portfolio platform demonstrating practical
    implementation of recognized construction disruption-analysis methodologies.

    It is a practical laboratory where construction methodologies are transformed into:

    - Transparent calculations
    - Visualisations
    - Forecasts
    - Interpretations

    The objective is not to automate claims preparation.

    The objective is to demonstrate practical understanding of disruption-analysis methodologies
    through implementation.
    """)

    st.markdown("---")

    st.header("Architecture")

    col1, col2 = st.columns(2)

    with col1:

        st.info("""
        **Module 1: Measured Mile**

        Answers:

        *How much productivity was lost during the disruption period compared with the measured mile period?*
        """)

        st.info("""
        **Module 2: Earned Value**

        Answers:

        *How did labour performance change during the disruption period?*
        """)

    with col2:

        st.info("""
        **Module 3: Total Unit Cost**

        Answers:

        *How did cost efficiency change during the disruption period?*
        """)

        st.info("""
        **Module 4: Disruption Assistant (AI)**

        Answers:

        *Which methodology is most suitable given the available records and project circumstances?*
        """)

    st.markdown("---")

    st.header("Technology Stack")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### Core

        - Python
        - Pandas

        ### Framework

        - Streamlit
        """)

    with col2:
        st.markdown("""
        ### Visualisation

        - Plotly
        - Power BI

        ### AI

        - OpenAI API
        """)

    st.markdown("---")

    st.header("Roadmap")

    st.markdown("""
    ✅ Foundation (2026)

    ✅ PraxisLab Framework

    🔄 Measured Mile

    ⏳ Earned Value

    ⏳ Total Unit Cost

    ⏳ AI Narrative Engine

    ⏳ Disruption Assistant
    """)

    st.markdown("---")

    st.success("Status: Framework Development")

# --------------------------------------------------
# PLACEHOLDER PAGES
# --------------------------------------------------

elif page == "Measured Mile":
    st.title("Measured Mile")
    st.info("Module under development.")

elif page == "Earned Value":
    st.title("Earned Value")
    st.info("Module under development.")

elif page == "Total Unit Cost":
    st.title("Total Unit Cost")
    st.info("Module under development.")

elif page == "Disruption Assistant":
    st.title("Disruption Assistant")
    st.info("Module under development.")