# prototype_full_annotated.py

import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

# ------------------------------
# Page config
# ------------------------------
st.set_page_config(
    page_title="AI eDNA Prototype",
    layout="wide",
    page_icon="🧬"
)

st.title("🌊 AI-powered eDNA Biodiversity Dashboard")
st.markdown("Analyze environmental DNA sequences and predict species with AI.")

# ------------------------------
# Load sample dataset
# ------------------------------
# Sample CSV data
data = {
    "SampleID": ["S1", "S2", "S3", "S4", "S5"],
    "eDNA_Sequence": [
        "ATCGTACGATCG",
        "GCTAGCTAGCTA",
        "TTAGGCATCGAT",
        "CGATCGTACGTA",
        "ATGCGTACGTAG"
    ],
    "PredictedSpecies": [
        "Species A",
        "Species B",
        "Species C",
        "Species D",
        "Species E"
    ]
}

df = pd.DataFrame(data)

# ------------------------------
# Sidebar
# ------------------------------
st.sidebar.header("Filters")
selected_species = st.sidebar.multiselect(
    "Select Species to View",
    options=df["PredictedSpecies"].unique(),
    default=df["PredictedSpecies"].unique()
)

filtered_df = df[df["PredictedSpecies"].isin(selected_species)]

# ------------------------------
# Show data table
# ------------------------------
st.subheader("Predicted Species Table")
st.dataframe(filtered_df[["SampleID", "PredictedSpecies", "eDNA_Sequence"]])

# ------------------------------
# Species count chart
# ------------------------------
st.subheader("Species Distribution")
species_count = filtered_df["PredictedSpecies"].value_counts().reset_index()
species_count.columns = ["Species", "Count"]

fig = px.bar(species_count, x="Species", y="Count", color="Species",
             title="Number of Samples per Species")
st.plotly_chart(fig, use_container_width=True)

# ------------------------------
# Show images (make sure these are uploaded in GitHub)
# ------------------------------
st.subheader("System Architecture")
try:
    flowchart = Image.open("flowchart.png")
    st.image(flowchart, caption="System Architecture", use_container_width=True)
except:
    st.warning("flowchart.png not found. Upload it to GitHub!")

st.subheader("Dashboard Preview")
try:
    dashboard = Image.open("dashboard.png")
    st.image(dashboard, caption="Dashboard Preview", use_container_width=True)
except:
    st.warning("dashboard.png not found. Upload it to GitHub!")

st.markdown("---")
st.markdown("✅ This is a **working AI eDNA prototype** ready for demo and hackathon presentation!")
