import json, re, os

Ingredients_aktuell = {}

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
        #print(rezept)
        inp = None
        while inp != ' ':
            inp = input('Press')

def OpenFile():
    with open('rezepte_test.json', 'r') as f:
        return json.load(f)





def SearchIngr(rezepte):
    Ingredients = {}
    for rezept in rezepte:

        for ingr in rezepte[rezept]['Zutaten']:

            ingr_temp = RegClean(str(rezepte[rezept]['Zutaten'][ingr]).replace('Anteil(e) ','').replace('Spritzer ', '')).replace('Schuss ', '').replace('Tasse','').replace('Kugel ','').replace('TL','').replace('BL','').replace('EL','').replace('MSp.','').replace('Stk.','').replace('Stk', '').strip()
            if ingr_temp in Ingredients:
                Ingredients[ingr_temp] += 1
            else:
                Ingredients[ingr_temp] = 1

    Ingredients_aktuell = Ingredients
    return Ingredients



def print_ing():
    print('Insgesamte Länge: ' + str(len(Ingredients)))
    for i in Ingredients:
        print(Ingredients)



def whitelisting(Ingredients, link):
    blacklist = {}
    os.remove('dump.json')
    with open ('dump.json', 'x') as dump:


        for ingr in Ingredients:
            if ingr not in blacklist:
                inp = input(ingr + "?:   ")
                if(inp == ''):
                    blacklist[ingr] = ingr
                    print(blacklist[ingr])

                if(inp == 'break'):
                    json.dump(blacklist, dump, indent=2)
                    break

                else:
                    blacklist[ingr] = inp
                    print(blacklist[ingr])
        json.dump(blacklist,dump,indent=2)





if __name__ == '__main__':
    link = 'rezepte_test.json'
    rezepte = OpenFile()
    Ingredients = SearchIngr(rezepte)
    whitelisting(Ingredients, link)
    print()










