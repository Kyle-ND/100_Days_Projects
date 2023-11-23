import random
from blackjack_art import logo
#assume infinite deck
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

computer_deck = []
user_deck = []

def deal(deck):
    card = random.choice(deck)
    return card

for i in range(2):
    computer_deck.append(random.choice(cards))
    user_deck.append(random.choice(cards))
print(logo)
print(f"Computer deck: {[computer_deck[0]]}")
print(f"Your deck: {user_deck}")

sum_usr = 0
for i in user_deck:
    sum_usr += i

sum_comp = 0
for i in computer_deck:
    sum_comp += i

if sum_usr <= 21:
    while True:
        r = input("would you like to deal or pass?: ")
        if r == 'pass':
            if sum_usr > sum_comp:
                if sum_usr <= 21:
                    if sum_usr < 17:
                        card = deal(cards)
                        user_deck.append(card)
                        sum_usr += card
                        if sum_usr > 21:
                            print(f"Computer deck: {computer_deck}")
                            print(f"Your deck: {user_deck}")
                            print("You lose")
                            break
                    print(f"Computer deck: {computer_deck}")
                    print(f"Your deck: {user_deck}")
                    print("You Win")
                    break
                else:
                    print(f"Computer deck: {computer_deck}")
                    print(f"Your deck: {user_deck}")
                    print("You Lose")
                    break
            elif sum_usr < sum_comp:
                if sum_comp <= 21:
                    if sum_comp < 17:
                        card = deal(cards)
                        computer_deck.append(card)
                        sum_comp += card
                        if sum_comp > 21:
                            print(f"Computer deck: {computer_deck}")
                            print(f"Your deck: {user_deck}")
                            print("You Win")
                            break
                    print(f"Computer deck: {computer_deck}")
                    print(f"Your deck: {user_deck}")
                    print("Computer Wins")
                    break
                else:
                    print(f"Computer deck: {computer_deck}")
                    print(f"Your deck: {user_deck}")
                    print("You Win")
                    break

            elif sum_usr == sum_comp:
                print(f"Computer deck: {computer_deck}")
                print(f"Your deck: {user_deck}")
                print("Draw")
                break
        elif r == "deal":
            card = deal(cards)
            user_deck.append(card)
            sum_usr += card
            if sum_usr > 21:
                print(f"Computer deck: {computer_deck}")
                print(f"Your deck: {user_deck}")
                print("you lose")
                break
            else:
                print(f"Computer deck: {[computer_deck[0]]}")
                print(f"Your deck: {user_deck}")
                


