import streamlit as st

from modules.measured_mile import show_measured_mile
# from modules.earned_value import show_earned_value
# from modules.total_unit_cost import show_total_unit_cost
# from modules.disruption_assistant import show_disruption_assistant

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

    st.subheader("Disruption Methodologies in Practice")

    st.markdown("---")

    st.markdown("""
    ## Vision

    PraxisLab is a professional portfolio platform demonstrating
    practical implementation of recognised construction productivity
    and disruption assessment methodologies.

    The platform transforms methodologies into:

    - Transparent calculations
    - Visualisations
    - Forecasts
    - AI-assisted interpretations

    """)

    st.markdown("---")

    st.header("Current Modules")

    st.markdown("""
    ✅ Measured Mile

    ⏳ Earned Value

    ⏳ Total Unit Cost

    ⏳ Disruption Assistant
    """)

# --------------------------------------------------
# MODULES
# --------------------------------------------------

elif page == "Measured Mile":
    show_measured_mile()

elif page == "Earned Value":
    st.title("Earned Value")
    st.info("Module under development.")

elif page == "Total Unit Cost":
    st.title("Total Unit Cost")
    st.info("Module under development.")

elif page == "Disruption Assistant":
    st.title("Disruption Assistant")
    st.info("Module under development.")