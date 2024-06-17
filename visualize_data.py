import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Läs in det förberedda datasetet
df = pd.read_csv('prepared_suicide_statistics.csv')

# Kontrollera att datasetet har laddats korrekt
print("Första raderna i det förberedda datasetet:")
print(df.head())

# Generera visualiseringar baserat på AI:s insikter

# 1. Trend över tid
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='year', y='suicide_rate', hue='country')
plt.title('Suicide Rates Over Time by Country')
plt.xlabel('Year')
plt.ylabel('Suicide Rate per 100,000')
plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# 2. Skillnader mellan kön över tid
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='year', y='suicide_rate', hue='sex')
plt.title('Suicide Rates by Sex Over Time')
plt.xlabel('Year')
plt.ylabel('Suicide Rate per 100,000')
plt.legend(title='Sex')
plt.show()

# 3. Skillnader mellan åldersgrupper
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='age', y='suicide_rate', hue='sex')
plt.title('Suicide Rates by Age Group and Sex')
plt.xlabel('Age Group')
plt.ylabel('Suicide Rate per 100,000')
plt.show()

# 4. Länder med högsta och lägsta självmordsfrekvens
mean_suicide_rates = df.groupby('country')['suicide_rate'].mean().reset_index()
top_countries = mean_suicide_rates.sort_values(by='suicide_rate', ascending=False).head(10)
bottom_countries = mean_suicide_rates.sort_values(by='suicide_rate').head(10)

plt.figure(figsize=(12, 6))
sns.barplot(data=top_countries, x='suicide_rate', y='country')
plt.title('Top 10 Countries with Highest Suicide Rates')
plt.xlabel('Suicide Rate per 100,000')
plt.ylabel('Country')
plt.show()

plt.figure(figsize=(12, 6))
sns.barplot(data=bottom_countries, x='suicide_rate', y='country')
plt.title('Top 10 Countries with Lowest Suicide Rates')
plt.xlabel('Suicide Rate per 100,000')
plt.ylabel('Country')
plt.show()
