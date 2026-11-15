import streamlit as st

st.set_page_config(
    page_title="PraxisLab",
    page_icon="📊",
    layout="wide"
)

st.title("PraxisLab")
st.subheader("Methodologies in Practice")

st.markdown("""
### Vision

PraxisLab is a professional portfolio platform demonstrating practical implementation of recognized construction disruption-analysis methodologies.

It is a practical laboratory where construction methodologies are transformed into:

- Transparent calculations
- Visualizations
- Forecasts
- Interpretations
""")

st.markdown("---")

st.header("Modules")

col1, col2 = st.columns(2)

with col1:
    st.info("Module 1: Measured Mile")
    st.info("Module 2: Earned Value")

with col2:
    st.info("Module 3: Total Unit Cost")
    st.info("Module 4: Disruption Assistant (AI)")

st.markdown("---")

st.success("PraxisLab v0.1")