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

liquids = content.find_all('span', {'class': 'unit'})

if len(liquids) > 0:

    for liq in liquids:
        # true wenn nächster tag kein sibling ist
        if liq.next_sibling != ' ':
            # Zutaten, die doppelt integriert sind
            if liq.next_sibling.endswith(', '):
                print(liq.next_sibling + liq.next_sibling.next_sibling.text + ': ' + liq.text)
            # Zutaten, die normal integriert sind
            else:
                print(liq.next_sibling + ': ' + liq.text)

        # nächstes Element ist ein Tag
        else:
            print(liq.find_next('a').text + ': ' + liq.text)


    #   Alle Zutaten, die ohne Menge integriert sind
    else:
        #   Alle <br> Tags finden -> max 5 Tags
        brs = liq.find_all_next('br', limit=5)
        for br in brs:
            #   Skippe leere siblings
            if br.next_sibling is None:
                break
            # für <a> tags
            if isinstance(br.next_sibling, Tag):
                print(' ' + str(br.next_sibling.text))
            # für Strings
            if isinstance(br.next_sibling, NavigableString):
                print(' ' + str(br.next_sibling))

else:
    pass


