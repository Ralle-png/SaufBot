slots_alk = [0,1,2,3,4,5,6]
slots_soft = [0,1,2,3,4]

def Slots ():
    for i in slots_alk:
        slots_alk[i] = input("Alkohol-Slot %d?\n" % i)
    for i in slots_soft:
        slots_soft[i] = input("Softdrink-Slot %d?\n" % i)
Slots()


print(slots_alk)
print(slots_soft)

