import random
import game_parts

game_parts.print_rules()

dealer_total = 0
player_total = 0
profit = 0

while True:
    choice2 = "0"
    bet = game_parts.get_value("Hoeveel euro wil je inzetten? ", float)

    deck = game_parts.reset_deck()
    random.shuffle(deck)

    dealer = game_parts.Dealer()
    player = game_parts.Player()

    dealer.dealer_add_card(deck.pop(0))
    dealer.dealer_add_card(deck.pop(0))

    player.player_add_card(deck.pop(0))
    player.player_add_card(deck.pop(0))

    def cacl_dealer_value():
        global dealer_total
        dealer_total = 0
        for card in dealer.dealer_show_card():
            dealer_total += card.show_value()

    def calc_player_value():
        global player_total
        player_total = 0
        for card in player.player_show_card():
            player_total += card.show_value()

    def print_cards(first_time):
        game_parts.new_line()
        print("#########################")
        print("Deler kaarten:")
        print("#########################")
        if first_time == True:
            print(dealer.dealer_show_card()[0].show_card())
            print("Gesloten kaart")
        else:
            for card in dealer.dealer_show_card():
                print(card.show_card())
        print("-------------------------")
        global dealer_total
        if first_time == True:
            dealer_total = 0
            dealer_total = dealer_total + dealer.dealer_show_card()[0].show_value()
        else:
            cacl_dealer_value()
        print(f"Totale punten: {dealer_total}")

        print("#########################")
        print("Jouw kaarten:")
        print("#########################")
        for card in player.player_show_card():
            print(card.show_card())
        print("-------------------------")
        calc_player_value()
        print(f"Totale punten: {player_total}")
        print("#########################")        

    while True:
        calc_player_value()
        for card in player.player_show_card():
            if player_total > 21 and card.show_ace() == True:
                card.change_value()
                calc_player_value()
        
        print_cards(True)
        
        if player_total == 21 and player.player_len_hand() == 2:
            choice2 = "2"

        elif player_total == 21:
            choice2 = "2"

        elif player_total > 21:
            break

        if choice2 == "2":
            pass

        else:
            print("1) HIT")
            print("2) CALL")
            choice2 = input("")

        match choice2:
            case "1":
                player.player_add_card(deck.pop(0))

                calc_player_value()

            case "2":
                cacl_dealer_value()

                while dealer_total <= 16:
                    dealer.dealer_add_card(deck.pop(0))

                    cacl_dealer_value()
                break
    
    if player_total > 21:
        profit -= bet
        print_cards(False)
        print("\U0001F534Je hebt meer dan 21 punten... Je hebt verloren! Je inzet is weggenomen!\U0001F534")

    elif player_total == 21 and player.player_len_hand() == 2:
        profit += bet * 1.5
        print_cards(False)
        print(f"\U0001F7E2Je hebt blackjack! Je hebt je inzet teruggekregen en nog een {bet * 1.5} euro erbij gekregen!\U0001F7E2")

    elif dealer_total > 21:
        profit += bet
        print_cards(False)
        print(f"\U0001F7E2De deler heeft meer dan 21 punten... Je hebt gewonnen! Je hebt je inzet teruggekregen en nog eens {bet} euro erbij gekregen!\U0001F7E2")

    elif dealer_total < player_total:
        profit += bet
        print_cards(False)
        print(f"\U0001F7E2Je hebt meer punten dan de deler... Je hebt gewonnen! Je hebt he inzet teruggekregen en nog eens {bet} euro erbij gekregen!\U0001F7E2")

    elif dealer_total == player_total:
        print_cards(False)
        print("\U0001F534Jij en de deler hebben hetzelfde aantal punten... Het is gelijkspel! Je hebt je inzet teruggekregen!\U0001F534")

    else:
        profit -= bet
        print_cards(False)
        print("\U0001F534De deler heeft meer punten dan jou... Je hebt verloren! Je inzet is weggenomen\U0001F534")

    if profit >= 0:
        print(f"Je hebt in totaal {profit} euro gewonnen!")
    else:
        print(f"Je hebt in totaal {-profit} euro verloren!")

    print("Wil je nog een keer spelen?")
    print("1) Ja")
    print("2) Nee")
    choice3 = input("")

    match choice3:
        case "1":
            continue

        case "2": 
            print("Oke doei!")
            break