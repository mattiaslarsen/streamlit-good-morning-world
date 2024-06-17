import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Test Deploy Plotly")

# Skapa exempeldata
df = pd.DataFrame({
    "x": [1, 2, 3, 4],
    "y": [10, 20, 30, 40]
})

# Skapa en enkel plot med plotly
fig = px.line(df, x="x", y="y", title="Simple Line Plot")

# Visa ploten i Streamlit
st.plotly_chart(fig)
