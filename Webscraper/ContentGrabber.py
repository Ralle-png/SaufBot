from urllib.request import urlopen as rq
from bs4 import BeautifulSoup
import re

#37-thirtyseven
#aperol-royal
#austrian-absolute-55
#apfelcaipirinha
#bahama-bay
#43er-ed-von-schleck
#abseitsfalle

def grabContent(link):
    list_client = rq('https://www.mixable.de' + link)
    html_normal = list_client.read()
    list_client.close()
    content = BeautifulSoup(html_normal, 'html.parser')

    Container = content.find('div', {'class': 'd-flex justify-content-center'})
    AlkGehalt = content.find('span', {'class': 'text-nowrap'}).text
    Bewertung = content.find('span', {'class' : 'rating-result'}).text
    print(Bewertung)

    inhalt = Container.text.replace("Einheit anpassen ...cl (Zentiliter)ml (Milliliter)oz (Fluid Ounce)l (Liter)Einheiten zurücksetzen ", "").replace("\n","").replace("Licor 43", "Licor43 ").replace('Ginger Ale', 'Gingerale').replace('28','Twentyeight').replace('Sweet & Sour', 'Sweetsour').replace('Bitter Lemon', 'Bitterlemon').replace('Tonic Water', 'Tonicwater').replace('Crushed Ice', 'Crushedice').replace("  ", " ")
    print('\n' + inhalt)

    pattern1 = re.compile("(\B|\))[A-Z][a-z]+")
    pattern2 = re.compile("[0-9,./]{0,4} (cl|ml|l|oz|g|Schuss|Spritzer|Anteil(e)|Tasse|Kugel|TL|BL|EL|MSp.|Stk.)?(\s)?[A-Za-zÄÖÜ()][a-zäöüñçèéúß()%-]+(43)?((\s|,|,\s)[A-ZÄÖÜ()][a-zäöüñçèéú%()]+)*")

    matches1 = pattern1.finditer(inhalt)
    matches2 = pattern2.finditer(inhalt)


    i = 0
    zutaten_dict = {}
    for match in matches2:
        s = match.start()
        e = match.end()
        i += 1
        zutaten_dict['ingr' + str(i)] = inhalt[s:e]
        print(inhalt[s:e])

    for match in matches1:
        s = match.start()
        e = match.end()
        i += 1
        zutaten_dict['ingr' + str(i)] = inhalt[s:e].replace(")","")
        print(inhalt[s:e].replace(")",""))

    print(AlkGehalt + '\n' )

    return {'Zutaten':zutaten_dict, 'AlkGehalt': AlkGehalt, 'Plaintext' : inhalt, 'Bewertung' : Bewertung}
