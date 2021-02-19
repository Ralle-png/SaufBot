from bs4 import BeautifulSoup
from urllib.request import urlopen as rq
from time import sleep
import json


from Webscraper.ContentGrabber import grabContent

rezepte = {}


def html(seite):
    list_client = rq(seite)
    html_normal = list_client.read()
    list_client.close()
    return BeautifulSoup(html_normal, 'html.parser')


for k in range(1,34):
    main_seite = 'http://www.mixable.de/recipes?page=' + str(k)
    list_soup = html(main_seite)
    mainpaige = list_soup.find("div", {"itemtype": "http://schema.org/CollectionPage"})
    cocktails = mainpaige.find_all("tr", {"itemprop": "itemListElement"})

    for cocktail in cocktails:
        # Cocktail Name
        cocktail_name = cocktail.a.text
        print('+++' + cocktail_name + '+++')

        # Cocktail Seite laden
        cocktail_link = cocktail.find("td").a["href"]
        rezepte[cocktail_name] = grabContent(cocktail_link)
        sleep(0.2)

with open('rezepte.json', 'w') as f:
    json.dump(rezepte, f, indent=2)