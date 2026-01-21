'''Met het opslaan van de text file heb ik hulp gehad van ai. de rest heb ik zelf gemaakt.'''

class spellen():
    def __init__(self, naam, prijs):
        self.naam = naam
        self.prijs = prijs

    def print_spellen(self, nummer):
        print(f"Spel nummer {nummer} heet {self.naam} en het kost {self.prijs} euro.")
    
    def geef_prijs(self):
        return self.prijs
    
    def goed_opslaan(self):
        return f"{self.naam};{self.prijs}"
    
def get_value(text, data_type):
    while True:
        try:
            return data_type(input(text))
        except:
            print("Dit is een incorrect datatype, probeer het opnieuw!")

mijn_spellen = []

print("Welkom bij je wishlist!")

while True:
    print("1) Ga verder met vorige wishlist")
    print("2) Maak een nieuwe wishlist (zal vorige wishlists verwijderen)")
    nieuw_oud = input("")
    if nieuw_oud == "1":
        with open("huiswerk/wishlist_objecten.txt", "r") as input_file:
            regels = input_file.readlines()

        for index, regels in enumerate(regels):
            schone_regel = regels.strip()

            delen = schone_regel.split(";")

            naam = delen[0]
            prijs_string = delen[1].strip()
            prijs = float(prijs_string)

            mijn_spellen.append(spellen(naam, prijs))
        print(f"Er zijn {len(mijn_spellen)} spellen succesvol geladen!")
        break
    elif nieuw_oud == "2":
        break
    else:
        print(f"{nieuw_oud} is geen geldige optie, probeer het opnieuw!")
        pass

while True:
    print("")
    print("1) Spellen bekijken")
    print("2) Spel toevoegen")
    print("3) Spel aanpassen/verwijderen")
    print("4) Totaalprijs berekenen")
    print("5) Aflsuiten")
    keuze = input("")
    print("")

    if keuze == '1':
        if len(mijn_spellen) == 0:
            print("Er zitten nog geen spellen in je wishlist!")
        else:
            index = 1
            for spel in range(len(mijn_spellen)):
                mijn_spellen[spel].print_spellen(index)
                index += 1

    elif keuze == "2":
        spel_naam = input("Hoe heet het spel die je wilt toevoegen? ")
        spel_prijs = get_value("En hoe duur is dat spel in euro's? ", float)
        spel_index = len(mijn_spellen)
        mijn_spellen.append(spellen(spel_naam, spel_prijs))
        print("Oke, toegevoegd!")

    elif keuze == "3":
        print("Wil je een spel")
        print("1) Verwijderen")
        print("2) Aanpassen")
        verw_aanp = input("")
        welk_spel = get_value("Welk nummer heeft het spel die je wilt aanpassen of verwijderen? ", int)
        if verw_aanp == "1":
            mijn_spellen.pop(welk_spel - 1)

        elif verw_aanp == "2":
            nieuwe_naam = input("Wat is de nieuwe naam? ")
            nieuwe_prijs = get_value("Wat is de nieuwe prijs? ", float)
            mijn_spellen[welk_spel - 1] = spellen(nieuwe_naam, nieuwe_prijs)
        print("Het spel is aangepast of verwijderd!")

    elif keuze == "4":
        totaal_prijs = 0
        for spel in range(len(mijn_spellen)):
            totaal_prijs = totaal_prijs + mijn_spellen[spel].geef_prijs()
        if totaal_prijs == 0:
            print("Je hebt nog geen spellen toegevoegd, of de spellen zijn gratis!")
        else:
            print(f"De totale prijs van al je spellen is {round(totaal_prijs, 2)} euro.")

    elif keuze == "5":
        while True:
            print("1) Wishlist opslaan")
            print("2) Wishlist niet opslaan")
            opslaan = input("")

            if opslaan == "1":
                with open("huiswerk/wishlist_objecten.txt", "w") as output_file:
                    for spel in mijn_spellen:
                        output_file.write(spel.goed_opslaan() + "\n")
                print("Je wishlist is succesvol opgeslagen!")
                print("doei!")
                break

            elif opslaan == "2":
                print("doei!")
                break

            else:
                print(f"{opslaan} is geen geldige optie!")
                pass
        break

    else:
        print(f"{keuze} is geen geldige optie!")
        pass