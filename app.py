import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
data = pd.read_csv("cleaned_2015.csv")

# Title
st.title("🌍 Public Dataset Storytelling App")

st.write("Analyze global happiness trends using data.")

# Show dataset
st.subheader("📊 Dataset Preview")
st.dataframe(data.head())

# Sidebar filter
st.sidebar.header("Filter Data")
selected_country = st.sidebar.selectbox(
    "Select Country", data["Country"].unique()
)

filtered_data = data[data["Country"] == selected_country]

# Scatter plot (FIXED COLUMN NAMES)
st.subheader("📈 GDP vs Happiness")

fig1 = px.scatter(
    data,
    x="Economy_(GDP_per_Capita)",
    y="Happiness_Score",
    hover_name="Country",
    title="GDP vs Happiness"
)

st.plotly_chart(fig1)

# Top 10 countries
st.subheader("🏆 Top 10 Happiest Countries")

top10 = data.sort_values(
    by="Happiness_Score", ascending=False
).head(10)

fig2 = px.bar(
    top10,
    x="Country",
    y="Happiness_Score",
    title="Top 10 Happiest Countries"
)

st.plotly_chart(fig2)

# Insights (FIXED COLUMN NAMES)
st.subheader("🧠 Insights")

correlation = data["Economy_(GDP_per_Capita)"].corr(
    data["Happiness_Score"]
)

st.write(f"👉 Correlation between GDP and Happiness: {correlation:.2f}")

st.write("👉 Countries with higher GDP tend to have higher happiness.")

st.write("👉 Nordic countries dominate top rankings.")

# Selected country details
st.subheader("🌎 Selected Country Analysis")

st.write(filtered_data)

st.success("✅ Project Completed Successfully!")