import json
import re


def OpenFile(file):
    with open(file, 'r') as file:
        return json.load(file)


Ingredients = {}


def SearchIngr_old():
    global rezept
    for rezept in rezepte:

        for ingr in rezepte[rezept]['Zutaten']:

            ingr_temp = RegClean(str(rezepte[rezept]['Zutaten'][ingr]).replace('Anteil(e) ','').replace('Spritzer ', '')).replace('Schuss ', '').replace('Tasse','').replace('Kugel ','').replace('TL','').replace('BL','').replace('EL','').replace('MSp.','').replace('Stk.','').replace('Stk', '').strip()
            if ingr_temp in Ingredients:
                Ingredients[ingr_temp] += 1
            else:
                Ingredients[ingr_temp] = 1


    print('Insgesamte Länge: ' + str(len(Ingredients)))
    for i in Ingredients:
        print(i + ': ' + str(Ingredients[i]))



def IngrSearch():



def RegClean(ingr):
    try:
        #print(ingr)
        pattern = re.compile('[A-ZÄÖÜ][a-zäöüñçèéúß()%-_]+(43)?((\s|,|,\s)[A-ZÄÖÜ()][a-zäöüñçèéú%()]+)*')
        match = re.search(pattern,ingr)
        s = match.start()
        e = match.end()
        word = str(ingr[s:e])
        #print(word.strip())
        return word

    except AttributeError:
        print(rezept)
        inp = None
        while inp != ' ':
            inp = input('Press')



if __name__ == '__main__':
    rezepte = OpenFile("re");
