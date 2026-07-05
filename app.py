import streamlit as st

st.set_page_config(page_title="Factors of Production", page_icon="🏭")

st.title("Factors of Production")
st.write("Learn the four things every economy needs to produce goods and services.")

topic = st.selectbox(
    "Choose a topic:",
    ["Entrepreneurship", "Land", "Labour", "Capital"]
)

content = {
    "Entrepreneurship": """
### Entrepreneurship
The skill of organizing the other three factors (land, labour, capital) 
to produce goods/services and take on business risk.
**Reward:** Profit
**Example:** A person starting a bakery, combining flour, workers, and ovens.
""",
    "Land": """
### Land
All natural resources used in production — soil, water, minerals, forests, etc.
**Reward:** Rent
**Example:** Farmland used to grow wheat, or crude oil extracted from the ground.
""",
    "Labour": """
### Labour
The physical and mental human effort put into producing goods/services.
**Reward:** Wages
**Example:** Factory workers, teachers, doctors.
""",
    "Capital": """
### Capital
Man-made resources used to produce other goods — machinery, tools, buildings, money invested.
**Reward:** Interest
**Example:** A tractor used on a farm, or a computer used in an office.
"""
}

st.markdown(content[topic])

st.divider()
st.info("Together, these four factors combine to create everything a business produces.")
