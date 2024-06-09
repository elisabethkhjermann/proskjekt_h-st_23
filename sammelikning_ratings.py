# -*- coding: utf-8 -*-

# Sammenligning av de ulike nettsidenes rating

import json
import matplotlib.pyplot as plt
import numpy as np

filename = "movies-250.json"

with open(filename, encoding="utf-8") as file:
    data = json.load(file)

filmtitler_imdb = []
anmeldelser_imdb = []
film_dict_imdb = {}

filmtitler_RT = []
anmeldelser_RT = []
film_dict_RT = {}

filmtitler_metacritic = []
anmeldelser_metacritic = []
film_dict_metacritic = {}

for filmer in data["movies"]:
    title = filmer["Title"]
    ratings = filmer["Ratings"]

    for rating in ratings:
        if rating["Source"] == "Internet Movie Database":
            film_dict_imdb[title] = float(rating["Value"].replace("/10", ""))
        elif rating["Source"] == "Rotten Tomatoes":
            film_dict_RT[title] = int(rating["Value"].replace("%",""))
        elif rating["Source"] == "Metacritic":
            film_dict_metacritic[title]=int(rating["Value"].replace("/100", ""))

sorted_dict_imdb = sorted(film_dict_imdb.items(), key=lambda x: float(x[1]), reverse=True)

sorted_dict_RT = sorted(film_dict_RT.items(), key=lambda x: int(x[1]), reverse=True)

sorted_dict_metacritic = sorted(film_dict_metacritic.items(), key=lambda x: int(x[1]), reverse=True)

for movie in sorted_dict_imdb:
    filmtitler_imdb.append(movie[0])
    anmeldelser_imdb.append(movie[1])

for movie in sorted_dict_RT:
    filmtitler_RT.append(movie[0])
    anmeldelser_RT.append(movie[1])

for movie in sorted_dict_metacritic:
    filmtitler_metacritic.append(movie[0])
    anmeldelser_metacritic.append(movie[1])

# Sett størrelsen på figuren
fig2 = plt.figure(figsize=(12, 11))


# IMDb
plt.subplot(3, 1, 1)
plt.title("De ti filmene med høyest rating på IMDb", fontsize=15)
plt.grid(axis="x")
plt.xlabel("Ratings ut av 10", fontsize=12)
plt.ylabel("Filmer", fontsize=12)
plt.xticks(np.arange(0, 11, step=1))
plt.barh(filmtitler_imdb[:10][::-1], anmeldelser_imdb[:10][::-1])

# Rotten tomatoes
plt.subplot(3, 1, 2)
plt.title("De ti filmene med høyest rating på Rotten Tomatoes", fontsize=15)
plt.grid(axis="x")
plt.xlabel("hvor mange som stemte ja (%)", fontsize=12)
plt.ylabel("Filmer", fontsize=12)
plt.xticks(np.arange(0, 110, step=10))
plt.barh(filmtitler_RT[:10], anmeldelser_RT[:10], color="skyblue")

# Metacritic
plt.subplot(3, 1, 3)
plt.title("De ti filmene med høyest rating på Metacritic", fontsize=15)
plt.grid(axis="x")
plt.xlabel("Ratings ut av 100", fontsize=12)
plt.ylabel("Filmer", fontsize=12)
plt.xticks(np.arange(0, 110, step=10))
plt.barh(filmtitler_metacritic[:10], anmeldelser_metacritic[:10], color="lightblue")

plt.tight_layout(pad=2)
plt.show()