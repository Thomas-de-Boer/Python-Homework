'''
Thomas de Boer
Opdracht 1.1
12/09/2025
Dit programma maakt een aantal figuren met for loops.
'''

for x in range(5):
    print(5 * "*")

print("")

for x in range(1, 6):
    print(x * "*")

print("")

for x in range(5, 0, -1):
    print(x * "*")

print("")

for x in range(5):
    print("12345")

print("")

nummer_list = []
for x in range(1, 6):
    nummer_list.append(str(x))
    print("".join(nummer_list))

print("")

nummer_list = []
punt_list = [".", ".", ".", "."]
for x in range(1, 6):
    nummer_list.append(str(x))
    #nummers toevoegen aan de list
    print("".join(punt_list) + "".join(nummer_list))
    #de lists aan elkaar maken en printen
    if len(punt_list) == 0:
        punt_list.append(".")
    #een punt toevoegen voor als de list leeg is
    punt_list.pop()
    #een punt weghalen

print("")

'''
Thomas de Boer
Opdracht 1.2
12/09/2025
Dit programma doet hetzelfde als hierboven maar dan met while loops.
'''

x = 0
while x < 5:
    print("*****")
    x += 1

print("")

x = 1
while x < 6:
    print(x * "*")
    x += 1

print("")

x = 5
while x > 0:
    print(x * "*")
    x -= 1

print("")

x = 0
while x < 5:
    print("12345")
    x += 1

print("")

nummer_list = []
x = 1
while x < 6:
    nummer_list.append(str(x))
    print("".join(nummer_list))
    x += 1

print("")

nummer_list= []
punt_list = [".", ".", ".", "."]
x = 1
while x < 6:
    nummer_list.append(str(x))
    #nummers toevoegen aan de list
    print("".join(punt_list) + "".join(nummer_list))
    #de list aan elkaar maken en printen
    if len(punt_list) == 0:
        punt_list.append(".")
    #een punt toevoegen voor als de list leeg is
    punt_list.pop()
    #een punt weghalen
    x += 1

print("")

'''
Thomas de Boer
Opdracht 2
12/09/2025
Vraagt informatie over een figuur en print daarna dat figuur.
'''

grootte = int(input("Hoe groot moet het figuur zijn? "))

while grootte < 3:
    grootte = int(input("Het figuur moet tenminste een grootte hebben van 3. Hoe groot moet het figuur zijn? "))

binnen_symbool = input("Welk symbool moet er aan de binnenkant staan? ")
buiten_symbool = input("Welk symbool moet er aan de buitenkant staan? ")
#vragen stellen en variabelen declareren

print(grootte * buiten_symbool)
#bovenste rand printen
for x in range(grootte - 2):
    print(buiten_symbool + (grootte - 2) * binnen_symbool + buiten_symbool)
#binnenste vierkant en buiten randjes printen
print(grootte * buiten_symbool)
#onderste rand printen