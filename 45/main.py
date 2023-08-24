import requests
from bs4 import BeautifulSoup

response = requests.get(
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movies = response.text

soup = BeautifulSoup(movies, "html.parser")

titles = soup.find_all('h3', class_="title")
text_titles = [title.get_text() for title in titles]

movies = text_titles[::-1]

with open(file="45/movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie} \n")
