"""
This module contains a single function to run. This function, using functions created in the two modules it
imports from, does the following: creates a deck of 52 unique playing cards, shuffles them, and draws 5
random cards from the deck. After drawing 5 cards 100,000 times (the type of hand drawn is recorded for each
draw), the number of each type of hand and the percentage of times it was drawn is tabulated on a table.
"""

'''
I affirm that I have carried out the attached academic endeavors with full academic honesty, in
accordance with the Union College Honor Code and the course syllabus.
'''

from Categorization import *
from Cards import *


def play_rounds():
    """
    This function, using functions created in the two modules this file imports from, does the following:
    creates a deck of 52 unique playing cards, shuffles them, and draws 5 random cards from the deck.
    After drawing 5 cards 100,000 times (the type of hand drawn is recorded for each draw), the number
    of each type of hand and the percentage of times it was drawn is tabulated on a table.
    """

    flush = 0
    pair = 0
    two_pair = 0
    high_card = 0

    print('# of hands     pairs       %     2 pairs     %     flushes      %   high card       %')
    no_of_draws = 0
    deck = create_deck()
    ran_deck = random_deck(deck)

    while no_of_draws <= 100000:
        if ((no_of_draws % 10000) == 0) and (no_of_draws != 0):
            flush_percent = round(((flush / no_of_draws) * 100), 2)
            two_pair_percent = round(((two_pair / no_of_draws) * 100), 2)
            pair_percent = round(((pair / no_of_draws) * 100), 2)
            high_card_percent = round(((high_card / no_of_draws) * 100), 2)
            print(f'{no_of_draws:10,d}{pair:10,d}{pair_percent:10}{two_pair:10,d}   {two_pair_percent:05.6}{flush:10,d}    {flush_percent:05.6}{high_card:10,d}{high_card_percent:10}')

        hand = draw_hand(ran_deck)

        result = determine_hand(hand)
        if result == 1:
            flush += 1
        elif result == 2:
            two_pair += 1
        elif result == 3:
            pair += 1
        else:
            high_card += 1

        if len(ran_deck) == 2:
            deck = create_deck()
            ran_deck = random_deck(deck)

        no_of_draws += 1


play_rounds()
