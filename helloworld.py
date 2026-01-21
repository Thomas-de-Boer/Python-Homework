'''
Thomas de Boer
Opdracht 1
03/09/2025
Met dit programma kan ik mezelf snel en gemakkelijk voorstellen.
'''

naam = "Thomas"
leeftijd = 16
verjaardag = "29 April"
opleiding = "Software Developer"
slber = "Wouter"
geld_op_spaarrekening = 2.32
max_kilo_benchpress = 0.743

print("Opdracht 1")
print("Mijn naam is" , naam)
print("Ik ben" , leeftijd , "jaar oud")
print("Ik doe de opleiding" , opleiding)
print("Mijn slber is" , slber)
print("Ik heb" , geld_op_spaarrekening , "euro op mijn spaarrekening staan")
print("en mijn max benchpress is" , max_kilo_benchpress , "kilo")

print(" ")

'''
Thomas de Boer
Opdracht 2
03/09/2025
Met dit programma kan ik gemakkelijk berekeningen doen met een bepaald getal.
'''
print("Opdracht 2")
mijn_getal = 5
for x in range(2):
    print("Mijn getal is" , mijn_getal)
    print("Mijn getal keer 2 is" , mijn_getal * 2)
    print("De machtsverheffing van mijn getal is" , mijn_getal ** 2)
    print(mijn_getal * "Hallo ")
    print("Mijn getal gedeeld door 3 is" , mijn_getal / 3)
    print("Mijn getal gedeeld door 3 als een integer is" , int(mijn_getal / 3))
    print("De modulo van mijn getal met 3 is" , mijn_getal % 3)
    mijn_getal *= 2