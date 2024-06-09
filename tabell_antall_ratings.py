# -*- coding: utf-8 -*-

import json
import matplotlib.pyplot as plt
import numpy as np

filename = "movies-250.json"

with open(filename, encoding="utf-8") as file:
  data = json.load(file)

filmtitler = []
anmeldelser = []
film_dict_imdb = {}
votes_dict = {}
votes = []

for filmer in data["movies"]:
    film_dict_imdb[filmer["Title"]]=filmer["imdbRating"]
    votes_dict[filmer["Title"]] = filmer["imdbVotes"].replace(",","")

#høyeste
sorted_dict_imdb = sorted(film_dict_imdb.items(), key=lambda x: float(x[1]), reverse=True)

sorted_dict_votes = sorted(votes_dict.items(), key=lambda x: int(x[1]), reverse=True)

print(sorted_dict_votes[:10])

#høyeste
for movie in sorted_dict_imdb:
    filmtitler.append(movie[0])
    anmeldelser.append(float(movie[1]))

for movie in sorted_dict_votes:
    votes.append(movie[1])
print()

fig = plt.figure(figsize=(10, 4))

#Diagram 1
plt.title("De ti filmene med høyest rating på IMDb", fontsize=15)
plt.grid(axis="x")
plt.xticks(np.arange(0, 11, step=1))
plt.xlabel("Rating ut av 10", fontsize=12)
plt.ylabel("Filmer", fontsize=12)
plt.subplots_adjust(bottom=-0.6)
plt.barh(filmtitler[:10][::-1], anmeldelser[:10][::-1])
plt.show()

#Tabell
print("Film                                              |  Antall stemmer")
print("-------------------------------------------------------------------")

# Skriv ut tabellradene for de ti filmene med høyest IMDb-rating
for movie, vote in sorted_dict_votes[:10]:
    print(f"{movie.ljust(50)}| {vote.rjust(15)}")
    print("-------------------------------------------------------------------")



