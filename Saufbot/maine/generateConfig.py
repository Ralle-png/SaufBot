import json
from os import remove


def slot_init():

    slots = {'alk': {}, 'mische': {}, 'extra': {}}

    SLOTANZAHLALK = int(input("Wieviele Alkohole werden verwendet?: "))
    slots['alk']['anz'] = SLOTANZAHLALK
    SLOTANZAHLSOFT = int(input("Wieviele Mischgetränke werden verwendet?: "))
    slots['alk']['anz'] = SLOTANZAHLSOFT
    print("\n\n")

    for k in range(SLOTANZAHLALK):
        slot = 'alk' + str(k)
        slots['alk'][slot] = {'name': input("Alkohol-Slot %s?: " % k), 'preis': input("Preis der Flasche? (in Euro): "),
                              'inhalt' : input("Inhalt der Flasche? (in ml): ")}
        slots['alk'][slot]['fuellstand'] =  slots['alk'][slot]['inhalt']
        print("\n")


    print("------------------------------------------")
    print("------------------------------------------")
    print("\n\n")


    for k in range(SLOTANZAHLSOFT):
        slot = 'mische' + str(k)
        slots['mische'][slot] = {'name': input("Mische-Slot %s?: " % k), 'preis': input("Preis der Flasche? (in Euro): "),
                                 'inhalt': input("Inhalt der Flasche? (in ml): ")}
        slots['mische'][slot]['fuellstand'] = slots['mische'][slot]['inhalt']
        print("\n")


    print("\n")
    print(slots)


    try:
        remove('positions.json')
    except:
        pass
    finally:
        with open('positions.json', 'x') as dump:
            json.dump(slots, dump, indent=2)


slot_init()
