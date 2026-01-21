class Card():
    def __init__(self, name, value, ace):
        self.name = name
        self.value = value
        self.ace = ace

    def show_card(self):
        return self.name
    
    def show_value(self):
        return self.value
    
    def show_ace(self):
        return self.ace
    
    def change_value(self):
        self.value = 1

class Dealer():
    def __init__(self):
        self.hand = []

    def dealer_add_card(self, card):
        self.hand.append(card)

    def dealer_show_card(self):
        return self.hand
    
    def dealer_len_hand(self):
        return len(self.hand)

class Player():
    def __init__(self):
        self.hand = []

    def player_add_card(self, card):
        self.hand.append(card)

    def player_show_card(self):
        return self.hand
    
    def player_len_hand(self):
        return len(self.hand)
    
def new_line():
    for x in range(30):
        print()
    
def get_value(text, data_type):
    while True:
        try:
            return data_type(input(text))
        except:
            print("Dit is een incorrect datatype, probeer het opnieuw!")

def print_rules():
    while True:
        print("Welkom bij blackjack")
        print("1) Wil je dat de spelregels uitgelegd worden?")
        print("2) Of weet je de regels al")
        choice1 = input("")

        match choice1:
            case "1":
                print("De regels van blackjack zijn best simpel.")
                print("Elke kaart heeft een waarde.")
                print("Het doel is om 1: 21 punten te krijgen.")
                print("of 2: Om meer punten te hebben dan de deler.")
                print("Aan het begin krijg je twee kaarten van de deler.")
                print("De deler pakt ook twee kaarten voor zichzelf.")
                print("Een van die kaarten kan je zien, de andere niet.")
                print("je mag zoveel kaarten pakken als je wil.")
                print("Als de deler meer dan 21 punten heeft, dan win jij.")
                print("Als jij meer punten hebt dan de deler, maar minder dan 21, dan win jij.")
                print("Als je precies 21 punten hebt dan win jij automatisch.")
                input("Klik op enter om te beginnen met spelen!")
                print()
                break
            case "2":
                print()
                break
            case _:
                print("Dat is geen geldige optie!")
                print()
    
def reset_deck():
    return [
    Card("\u2660\uFE0F aas", 11, True),
    Card("\u2660\uFE0F 2", 2, False),
    Card("\u2660\uFE0F 3", 3, False),
    Card("\u2660\uFE0F 4", 4, False),
    Card("\u2660\uFE0F 5", 5, False),
    Card("\u2660\uFE0F 6", 6, False),
    Card("\u2660\uFE0F 7", 7, False),
    Card("\u2660\uFE0F 8", 8, False),
    Card("\u2660\uFE0F 9", 9, False),
    Card("\u2660\uFE0F 10", 10, False),
    Card("\u2660\uFE0F boer", 10, False),
    Card("\u2660\uFE0F dame", 10, False),
    Card("\u2660\uFE0F heer", 10, False),

    Card("\u2764\uFE0F aas", 11, True),
    Card("\u2764\uFE0F 2", 2, False),
    Card("\u2764\uFE0F 3", 3, False),
    Card("\u2764\uFE0F 4", 4, False),
    Card("\u2764\uFE0F 5", 5, False),
    Card("\u2764\uFE0F 6", 6, False),
    Card("\u2764\uFE0F 7", 7, False),
    Card("\u2764\uFE0F 8", 8, False),
    Card("\u2764\uFE0F 9", 9, False),
    Card("\u2764\uFE0F 10", 10, False),
    Card("\u2764\uFE0F boer", 10, False),
    Card("\u2764\uFE0F dame", 10, False),
    Card("\u2764\uFE0F heer", 10, False),

    Card("\u2666\uFE0F aas", 11, True),
    Card("\u2666\uFE0F 2", 2, False),
    Card("\u2666\uFE0F 3", 3, False),
    Card("\u2666\uFE0F 4", 4, False),
    Card("\u2666\uFE0F 5", 5, False),
    Card("\u2666\uFE0F 6", 6, False),
    Card("\u2666\uFE0F 7", 7, False),
    Card("\u2666\uFE0F 8", 8, False),
    Card("\u2666\uFE0F 9", 9, False),
    Card("\u2666\uFE0F 10", 10, False),
    Card("\u2666\uFE0F boer", 10, False),
    Card("\u2666\uFE0F dame", 10, False),
    Card("\u2666\uFE0F heer", 10, False),

    Card("\u2663\uFE0F aas", 11, True),
    Card("\u2663\uFE0F 2", 2, False),
    Card("\u2663\uFE0F 3", 3, False),
    Card("\u2663\uFE0F 4", 4, False),
    Card("\u2663\uFE0F 5", 5, False),
    Card("\u2663\uFE0F 6", 6, False),
    Card("\u2663\uFE0F 7", 7, False),
    Card("\u2663\uFE0F 8", 8, False),
    Card("\u2663\uFE0F 9", 9, False),
    Card("\u2663\uFE0F 10", 10, False),
    Card("\u2663\uFE0F boer", 10, False),
    Card("\u2663\uFE0F dame", 10, False),
    Card("\u2663\uFE0F heer", 10, False),
    ]