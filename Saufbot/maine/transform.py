import re, json

with open('dump.json', 'r') as dict, open('rezepte_test.json', 'r') as chg:
    dict = json.load(dict)
    dump = json.load(chg)

    for rezept in dump:
        for ing in dump[str(rezept)]['Zutaten']:
            ingr = dump[str(rezept)]['Zutaten'][ing]
            print(ingr)
            pattern = re.compile('[A-ZÄÖÜ][a-zäöüñçèéúß()%-_]+ ([A-ZÄÖÜ()][a-zäöüñçèéú%()]*)*')
            matches = pattern.search(ingr)
            if(matches != None):
                result = matches.span()
                ingr = re.sub(ingr[matches.start() : matches.end()], 'A',dump[str(rezept)]['Zutaten'][ing])
                print(ingr)






if '__name__' == '__main__':
    pass