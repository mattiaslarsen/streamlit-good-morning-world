import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
fig, ax = plt.subplots()
sns.lineplot(data=df[df['country'] == country], x='year', y='suicide_rate', hue='sex', ax=ax)
ax.set_title(f'Suicide Rates Over Time in {country}')
ax.set_xlabel('Year')
ax.set_ylabel('Suicide Rate per 100,000')
st.pyplot(fig)

# Bar plot för åldersgrupper och kön
fig, ax = plt.subplots()
sns.barplot(data=filtered_data, x='age', y='suicide_rate', hue='sex', ax=ax)
ax.set_title(f'Suicide Rates by Age Group and Sex in {country} for {year}')
ax.set_xlabel('Age Group')
ax.set_ylabel('Suicide Rate per 100,000')
st.pyplot(fig)
