from urllib.request import urlopen as rq
from bs4 import BeautifulSoup, NavigableString, Tag
link = input('')
cocktail_link = 'https://www.mixable.de/recipes/view/' + link

# HTML ziehen
list_client = rq(cocktail_link)
html_normal = list_client.read()
list_client.close()
content = BeautifulSoup(html_normal, 'html.parser')

# Webscraper-Container finden -> Wo die Zutaten sind
Container = content.find('div', {'class': 'd-flex justify-content-center'})

if Container.div.find_next()
    print()