# -*- coding: utf-8 -*-

import json
import csv
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize = (10,7))

# Avkastning

filename = "movies-250.json"

with open(filename, encoding="utf-8") as file:
    data = json.load(file)

aarstall = []
avkastning = []
film_dict = {}


# Oppretter en liste med egendefinerte navn på verdiene på x-aksen
y_labels = [f"${i} millioner" for i in np.arange(100, 1000, step=100)]


for movie in data["movies"]:
    if int(movie["Year"]) >= 1980:
        title = movie["Title"]
        # Sjekker om avkastningsverdien er 'N/A' før konvertering
        if movie["BoxOffice"] != 'N/A':
            box_office = float(movie["BoxOffice"].replace('$', '').replace(',', ''))
        info_arr = [int(movie["Year"]), box_office]
        film_dict[title] = info_arr


# Sorterer dictionaryen basert på avkastning
sorted_dict = sorted(film_dict.items(), key=lambda x: x[1][0])
#print(sorted_dict)

for movie in sorted_dict:
    aarstall.append(movie[1][0])
    avkastning.append(movie[1][1])

plt.subplot(2,1,1)
plt.plot(aarstall, avkastning)
plt.xlabel("År")
plt.xticks(np.arange(1980, 2023, step=5))
plt.ylabel("Avkastning")
# Bruker de egendefinerte y-akse etikettene
plt.yticks(np.arange(100000000, 1000000000, step=100000000), y_labels)
plt.title("De 10 filmene med høyest avkastning")
plt.grid(axis="y", linestyle='--')



# Inflasjon

# Åpner og leser CSV-filen
with open('inflasjon.csv', newline='') as csvfile:
    data = csv.DictReader(csvfile, delimiter=';')
    
    # Hopper over første linja
    overskrifter = next(data)
    
    year = []
    inflation = []

    # Leser data fra CSV-filen og lagrer i listene
    for row in data:
        year.append(int(row['year']))
        inflation.append(float(row['inflation'].replace('%', ' ')))


plt.subplot(2,1,2)
plt.plot(year, inflation, color='red')
plt.xlabel('År')
plt.ylabel('Inflasjon (%)')
plt.title('Inflasjon i USA (1980-2022)')
plt.xticks(np.arange(1980, 2023, step=5))
plt.grid(axis='y', linestyle='--')

# Viser diagrammene
plt.tight_layout(pad = 2)
plt.show()