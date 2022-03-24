import re, json

with open('dump.json', 'r') as dict, open('rezepte_.json', 'r') as chg:
    dict = json.load(dict)
    dump = json.load(chg)

    for rezept in dump:
        for ing in dump[str(rezept)]['Zutaten']:
            ingr = dump[str(rezept)]['Zutaten'][ing]
            #print(ingr)
            pattern = re.compile('[A-Z][A-Za-zäöüñçèéúß%-_\s\(\)]+')
            matches = pattern.search(ingr)
            if(matches != None):
                result = matches.span()
                ingr = re.sub(ingr[matches.start() : matches.end()], '',dump[str(rezept)]['Zutaten'][ing])
                print(ingr)






if '__name__' == '__main__':
    pass