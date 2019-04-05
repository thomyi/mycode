#!/usr/bin/env python3

from random import shuffle
# Blackjack game
print("Welcome to our Blackjack Game!")
while True:
    # Need a horn of cards / dealer deck
    deck = [ "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K" ]
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
    total_deck = []

    for suit in suits:
        for card in deck:
            total_deck.append(str(card) + "of " + suit) 

    print(len(total_deck))

    total_deck = total_deck * 6
    print(len(total_deck))

    shuffle(total_deck)
    print(total_deck)

    # Need a dealer hand
    # if total hand < 16, do another hit
    dealer_hand = []

    # Need a player hand
    player_hand = []

    # Need a loop to keep a game going on forever

    # Deal hands
    for x in range(2):
        dealer_hands.append(total_deck.pop())
        player_hands.appened(total_deck.pop())
   print(dealer_hand, player_hand)
   # Game logic
   # Card totals
   while True:
       x = input("Do you want another card?")
       another_card = input("Do you want another card?")
       
   # Do you want to play again?"
   x = input("Do yoou want to play again? ")
   if x.lower() == "n" or x.lower() == "no":
       break
