#usr/bin/python/
import random
import sys
import keyboard

deck = ["A♣", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "J♣", "Q♣", "K♣", "A♦", "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "J♦", "Q♦", "K♦", "A♥", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥", "Q♥", "K♥", "A♠", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠"]
def shuffle_deck(deck_tbs):
    random.shuffle(deck_tbs)
def print_deck(deck_tbp):
    print("Current Order of Deck:")
    print(deck_tbp)

print_deck(deck)    
print ("Press ENTER key to shuffle deck, ctrl+c to exit")
while True:
    try:
        if keyboard.is_pressed('ENTER'):
            shuffle_deck(deck)
            print_deck(deck)
            print ("Press ENTER key to shuffle deck again, ctrl+c to exit")
            keyboard.wait('ENTER')
    except:
        break
