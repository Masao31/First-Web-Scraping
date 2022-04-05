import requests
import numpy as np
from bs4 import BeautifulSoup

url = "https://www.lefigaro.fr/cinema/2017/06/28/03002-20170628ARTFIG00180-les-100-meilleurs-films-de-tous-les-temps-selon-les-lecteurs-du-magazine-empire.php"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#On récupère les titres de films mais il ny a pas de nom de class pour chaque em
liste = soup.find_all("em")

#On met les éléments dans une liste string
listeFilms = []
for film in liste:
    listeFilms.append(film.string)

#On supprime les 13 éléments en trop au début de la page qui ne sont pas dans la liste de films
for i in range(13):
    listeFilms.pop(0)


#On affiche pour vérifier
print(listeFilms)

fichier = open("liste.csv", "w")
np.savetxt("liste.csv", listeFilms, delimiter =",",fmt ='% s')
