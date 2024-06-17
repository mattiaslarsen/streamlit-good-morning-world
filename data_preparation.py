import pandas as pd

# Läs in datasetet
df = pd.read_csv('who_suicide_statistics.csv')

# Visa de första raderna i datasetet för att bekräfta att det har laddats korrekt
print("Första raderna i det ursprungliga datasetet:")
print(df.head())
print("\nKolumner i datasetet:")
print(df.columns)

# Välj relevanta kolumner
df = df[['country', 'year', 'age', 'sex', 'suicides_no', 'population']]
print("\nDataset efter att ha valt relevanta kolumner:")
print(df.head())

# Beräkna självmordsfrekvens per 100,000 personer
df['suicide_rate'] = df['suicides_no'] / df['population'] * 100000
print("\nDataset efter att ha beräknat självmordsfrekvens per 100,000 personer:")
print(df.head())
# Spara det förberedda datasetet till en ny CSV-fil
df.to_csv('prepared_suicide_statistics.csv', index=False)
print("\nDet förberedda datasetet har sparats till 'prepared_suicide_statistics.csv'.")
