from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/newest")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")

a_title = soup.find_all(class_='titleline')
titles = []
links = []
span_scores = soup.find_all('span', class_='score')
scores = [int(score.get_text().split()[0]) for score in span_scores]

for a in a_title:
    element = a.find('a')
    titles.append(element.get_text())
    links.append(element["href"])

for i in range(len(titles)):
    print(titles[i])
    print(links[i])
    print(scores[i])
""" # import xml
with open(file="45/website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title)
print(soup.title.string)
all_ancor_tags = soup.find_all(name="a")
print(all_ancor_tags)

for tag in all_ancor_tags:
    print(tag.getText())
    print(tag.get("href"))
 """
