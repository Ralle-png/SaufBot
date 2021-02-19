from urllib.request import urlopen as rq
from bs4 import BeautifulSoup
import re
import json

#37-thirtyseven
#aperol-royal
#austrian-absolute-55
#apfelcaipirinha
#bahama-bay
#43er-ed-von-schleck
#abseitsfalle

list_client = rq('https://www.mixable.de/recipes/view/abacaxi-caipirinha')
html_normal = list_client.read()
list_client.close()
content = BeautifulSoup(html_normal, 'html.parser')

Container = content.find('div', {'class': 'd-flex justify-content-center'})
AlkGehalt = content.find('span', {'class': 'text-nowrap'}).text

inhalt = Container.text.replace("Einheit anpassen ...cl (Zentiliter)ml (Milliliter)oz (Fluid Ounce)l (Liter)Einheiten zurücksetzen ", "").replace("\n","").replace("Licor 43", "Licor43 ").replace("  ", " ")

print(inhalt + '\n')

pattern1 = re.compile("(\B|\))[A-Z][a-z]+")
pattern2 = re.compile("[0-9,.]{1,4} (cl|ml|l|oz|g|Schuss|Spritzer|Anteil(e)|Kugel|TL|BL|EL|MSp.|Stk.)?(\s)?[A-ZÄÖÜ()][a-zäöüñçèéú()%-]+(43)?((\s|,|,\s)[A-ZÄÖÜ()][a-zäöüñçèéú%()%]+)*")

matches1 = pattern1.finditer(inhalt)
matches2 = pattern2.finditer(inhalt)

#   Matches mit Einheit
for match in matches2:
    s = match.start()
    e = match.end()
    print(inhalt[s:e])

#   Matches ohne Einheit
for match in matches1:
    s = match.start()
    e = match.end()
    print(inhalt[s:e].replace(")",""))

print('\n' + AlkGehalt)