def slot_init():

    alk_ = {'slot' : '', 'preis': '', 'inhalt' : ''}

    soft_slot = {}
    soft_preis = {}
    soft_inhalt = {}

    try:
        SLOTANZAHLALK = int(input("Wieviele Alkohole werden verwendet?: "))
        SLOTANZAHLSOFT = int(input("Wieviele Mischgetränke werden verwendet?: "))

        print("\n\n")

        for k in range(SLOTANZAHLALK):
            AlkAktuell = input("Alkohol-Slot %s?: " % k)
            alk_slot[AlkAktuell] = k
            alk_preis[alk_slot[AlkAktuell]] = input("Preis der Flasche? (in Euro): ")
            alk_inhalt[alk_slot[AlkAktuell]] = input("Inhalt der Flasche? (in Cl): ")
            print("\n")

        print("------------------------------------------")
        print("------------------------------------------")
        print("\n\n")

        for k in range(SLOTANZAHLSOFT):
            SoftAktuell = input("Softgetränk-Slot %s?: " % k)
            soft_slot[SoftAktuell] = k
            soft_preis[soft_slot[SoftAktuell]] = input("Preis des Softgetränks? (in Euro): ")
            soft_inhalt[soft_slot[SoftAktuell]] = input("Inhalt des Softgetränks? (in Cl): ")
            print("\n")
    except:
        print("Ein Fehler ist aufgetreten, versuchen sie es erneut!\n\n")
        slot_init()


    print(alk_slot)
    print(alk_preis)
    print(alk_inhalt)

    print(soft_slot)
    print(soft_preis)
    print(soft_inhalt)


slot_init()
