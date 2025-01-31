import matplotlib
matplotlib.use('Agg')  # Gebruik een niet-interactieve backend
import matplotlib.pyplot as plt

# gegevens als dictionary
data = {
    2015: 1000000,
    2016: 1050000,
    2017: 1100000,
    2018: 1150000,
    2019: 1200000,
    2020: 1250000,
    2021: 1300000,
    2022: 1350000,
    2023: 1400000,
    2024: 1450000
}

# Lijsten initialiseren
years = list(data.keys())
num_households = list(data.values())

# Maak de grafiek
plt.figure(figsize=(12, 8))  # Vergroot de figuur
plt.plot(years, num_households, marker='o')

# Grafiektitels en labels
plt.title('Huishoudens met problematische schulden in Nederland (2015-2024) volgens CBS')
plt.xlabel('Jaartal')
plt.ylabel('Aantal huishoudens')
plt.grid(True)

# Voeg annotaties toe
for i, txt in enumerate(num_households):
    plt.annotate(f'{txt:,}', (years[i], num_households[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Alle jaartallen op de x-as weergeven
plt.xticks(years)

# Sla de grafiek op in een bestand
plt.savefig('problematische_schulden_nederland.png')
