from Webscraper.ContentGrabber import *
import json

with open('rezepte_fertig.json', 'r') as f:
    print(len(json.load(f)))


#grabContent('/recipes/view/43er-au-lait')
