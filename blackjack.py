##Blackjack / 21

import random

#Dealer cards
dealer_cards = []

#Player cards
player_cards = []

#Deal the cards
#Dealer cards
while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1, 11))
    if len(dealer_cards) == 2:
        print("Dealer has: X &", dealer_cards[1])

#Player cards
while len(player_cards) != 2:
    player_cards.append(random.randint(1, 11))
    if len(player_cards) == 2:
         print("You have: ", player_cards)

#Display the cards

#Sum dealer cards
if sum(dealer_cards) == 21:
    print("Dealer has 21 and wins!")
elif sum(dealer_cards) > 21:
    print("Dealer has busted!")

#Sum player cards
while sum(player_cards) < 21:
    action_taken = str(input("Do you want to stick or twist? "))
    if action_taken == "twist":
        player_cards.append(random.randint(1, 11))
        print("You now have a total of " + str(sum(player_cards)) + " from these cards ", player_cards)
    else:
        print("The dealer has a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
        print("You have a total of " + str(sum(player_cards)) + " with ", player_cards)
        if sum(dealer_cards) > sum(player_cards):
            print("Dealer wins!")
        else:
            print("You win!")
            break

if sum(player_cards) > 21:
    print("You BUSTED! Dealer wins")
elif sum(player_cards) == 21:
    print("You have BLACKJACK! You Win!")



#Compare the sum of cards

#If P card sum > 21 BUST

#If P card sum is less than 21 Options Stick or Twist

#If P option Stay compare sum D vs P

#If P sum < 21 && > D then P wins

#If P sum < D sum then P loses