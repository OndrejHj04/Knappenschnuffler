import requests
from bs4 import BeautifulSoup
import sys

seite = "https://tickets.schalke04.de/de/events/auswaerts"

antwort = requests.get(seite)
antwort.encoding = "utf-8"
html = BeautifulSoup(antwort.text, "html.parser")

container = html.select_one("div.col-12.container")
grid = container.select_one("div.grid")

if not grid:
    with open("spiele.md", "w") as datei:
        datei.write('Keine Events gefunden')
    sys.exit()

spiele = grid.find_all("a")

markdown_inhalt = ""

for spiel in spiele:
    name = spiel.select_one("span.name").text
    tag = spiel.select_one('span.day').text
    monat = spiel.select_one('span.month').text

    markdown_inhalt += f"\n## {name}\n- Datum: {tag}. {monat}"


with open("spiele.md", "w") as datei:
    datei.write(markdown_inhalt)