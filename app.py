import streamlit as st

from modules.measured_mile import show_measured_mile

st.set_page_config(
    page_title="PraxisLab",
    page_icon="📊",
    layout="wide"
)

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

if page == "Home":

    st.title("PraxisLab")

    st.subheader(
        "Disruption Methodologies in Practice"
    )

    st.markdown("""
    Professional portfolio platform demonstrating
    practical implementation of recognized
    disruption-analysis methodologies.
    """)

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