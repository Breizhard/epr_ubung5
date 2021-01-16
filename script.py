"""Quartett"""
__author__ = "5641727, Redelin, 6544078, Kervella"

from random import shuffle
import time

amount_of_players = 5

cards = ['7\u2665', '7\u2666', '7\u2663', '7\u2660',
'8\u2665', '8\u2666', '8\u2663', '8\u2660',
'9\u2665', '9\u2666', '9\u2663', '9\u2660',
'10\u2665', '10\u2666', '10\u2663', '10\u2660',
'J\u2665', 'J\u2666', 'J\u2663', 'J\u2660',
'Q\u2665', 'Q\u2666', 'Q\u2663', 'Q\u2660',
'K\u2665', 'K\u2666', 'K\u2663', 'K\u2660',
'A\u2665', 'A\u2666', 'A\u2663', 'A\u2660']

shuffle(cards)
print("shuffling the cards ...")
time.sleep(2)

amount_of_cards = len(cards) 
cards_per_player = int(amount_of_cards/amount_of_players)
rest = amount_of_cards % amount_of_players  #Stapel
print(cards)
print("------------------")
print("Amount of cards:",amount_of_cards)
print("Cards per player:",cards_per_player)
print("The rest is:",rest)
print("------------------")

for i in range(0,amount_of_players):
    time.sleep(1)
    print("Player",i+1,"has the following cards:")
    print(cards[i*cards_per_player:(i+1)*cards_per_player])
