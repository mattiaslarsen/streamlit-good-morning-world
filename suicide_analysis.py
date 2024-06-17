import streamlit as st
import pandas as pd
import plotly.express as px

# Läsa in det förberedda datasetet
df = pd.read_csv('prepared_suicide_statistics.csv')

# Titel och introduktion
st.title("Global Suicide Rates Analysis")
st.write("This app visualizes global suicide rates using data from 1985 to 2016.")

# Interaktiva filter
country = st.selectbox('Select Country', df['country'].unique())
year = st.slider('Select Year', min_value=int(df['year'].min()), max_value=int(df['year'].max()), value=int(df['year'].mean()))

# Filtrera data
filtered_data = df[(df['country'] == country) & (df['year'] == year)]

# Visa grafer
st.subheader(f'Suicide Rates in {country} for {year}')

# Line plot över tid för valda landet
line_data = df[df['country'] == country]
fig1 = px.line(line_data, x='year', y='suicide_rate', color='sex', title='Suicide Rates Over Time')
st.plotly_chart(fig1)

# Bar plot för åldersgrupper och kön
fig2 = px.bar(filtered_data, x='age', y='suicide_rate', color='sex', barmode='group', title='Suicide Rates by Age Group and Sex')
st.plotly_chart(fig2)
