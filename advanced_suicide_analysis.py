import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Läsa in dataset
df = pd.read_csv('prepared_suicide_statistics.csv')

# Konvertera kolumner till rätt datatyp om nödvändigt
df['suicide_rate'] = pd.to_numeric(df['suicide_rate'], errors='coerce')
df['year'] = pd.to_numeric(df['year'], errors='coerce')

# Fyll NaN-värden med 0
df.fillna(0, inplace=True)

# Titel och introduktion
st.title("Advanced Global Suicide Rates Analysis")
st.write("This app provides advanced analysis of global suicide rates using data from 1985 to 2016.")

# Interaktiva filter
country = st.selectbox('Select Country', df['country'].unique())
year_range = st.slider('Select Year Range', min_value=int(df['year'].min()), max_value=int(df['year'].max()), value=(1990, 2010))

# Filtrera data
filtered_data = df[(df['country'] == country) & (df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Visa grafer
st.subheader(f'Suicide Rates in {country} from {year_range[0]} to {year_range[1]}')

# Välj endast numeriska kolumner
numeric_columns = ['year', 'suicide_rate']

# Aggrega data per år och kön
male_data = filtered_data[filtered_data['sex'] == 'male'][numeric_columns].groupby('year').mean().reset_index()
female_data = filtered_data[filtered_data['sex'] == 'female'][numeric_columns].groupby('year').mean().reset_index()

# Skapa figuren med linjär interpolering
fig1 = go.Figure()

fig1.add_trace(go.Scatter(
    x=male_data['year'],
    y=male_data['suicide_rate'],
    mode='lines+markers',
    name='Male',
    line_shape='linear'
))

fig1.add_trace(go.Scatter(
    x=female_data['year'],
    y=female_data['suicide_rate'],
    mode='lines+markers',
    name='Female',
    line_shape='linear'
))

fig1.update_layout(
    title=f'Suicide Rates Over Time in {country} ({year_range[0]}-{year_range[1]})',
    xaxis_title='Year',
    yaxis_title='Suicide Rate'
)

st.plotly_chart(fig1)

# Förbered data för referensstaplar och filtrerade data
total_data_male = df[(df['country'] == country) & (df['sex'] == 'male')]
total_data_female = df[(df['country'] == country) & (df['sex'] == 'female')]

total_data_male['filter'] = 'Total Male'
total_data_female['filter'] = 'Total Female'

filtered_data_male = filtered_data[filtered_data['sex'] == 'male']
filtered_data_female = filtered_data[filtered_data['sex'] == 'female']

filtered_data_male['filter'] = f'Male Filtered ({year_range[0]}-{year_range[1]})'
filtered_data_female['filter'] = f'Female Filtered ({year_range[0]}-{year_range[1]})'

combined_data_bar = pd.concat([total_data_male, total_data_female, filtered_data_male, filtered_data_female])

# Bar plot för åldersgrupper och kön för de filtrerade data
fig2 = px.bar(combined_data_bar, x='age', y='suicide_rate', color='filter', barmode='group', title=f'Suicide Rates by Age Group and Sex in {country} ({year_range[0]}-{year_range[1]})')
st.plotly_chart(fig2)

# Statistiska analyser för de filtrerade data
st.subheader("Statistical Analysis")
st.write(f"Mean suicide rate from {year_range[0]} to {year_range[1]}: {filtered_data['suicide_rate'].mean():.2f}")
st.write(f"Total suicides from {year_range[0]} to {year_range[1]}: {filtered_data['suicides_no'].sum()}")

# Prediktiva analyser (exempel med dummy data)
st.subheader("Predictive Analysis")
future_years = [2022, 2023, 2024]
predicted_rates = [12.5, 13.0, 13.5]  # Exempelvärden

fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=future_years, y=predicted_rates, mode='lines+markers', name='Predicted Rates'))
fig3.update_layout(title='Predicted Suicide Rates', xaxis_title='Year', yaxis_title='Suicide Rate')
st.plotly_chart(fig3)
