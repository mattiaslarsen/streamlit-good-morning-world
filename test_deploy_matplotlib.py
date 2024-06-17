import streamlit as st
import matplotlib.pyplot as plt

# Titel
st.title("Test Deploy Matplotlib")

# Kontrollera matplotlib version
st.write(f"Matplotlib version: {plt.__version__}")

# Skapa en enkel plot
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [10, 20, 25, 30])
ax.set_title("Simple Plot")

# Visa ploten i Streamlit
st.pyplot(fig)
