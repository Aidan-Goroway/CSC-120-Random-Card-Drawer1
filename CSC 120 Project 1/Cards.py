"""
This module contains the functions that will generate and randomize 52 unique cards.
"""
import random


def create_deck():
    """
    Creates a set of the 52 unique playing cards found within a deck.
    :return: Returns a deck of 52 playing cards.
    """
    deck = []
    rank_list = [str(2), str(3), str(4), str(5), str(6), str(7),
                 str(8), str(9), str(10), 'Jack', 'Queen', 'King', 'Ace']

    for rank in rank_list:
        deck.append(('Diamond', rank))
    for rank in rank_list:
        deck.append(('Heart', rank))
    for rank in rank_list:
        deck.append(('Spade', rank))
    for rank in rank_list:
        deck.append(('Club', rank))

    return deck


def random_deck(deck):
    """
    Randomizes the order of the deck of cards.
    :param: deck: The deck of cards, denoted as 'base' because it is still ordered.
    :return: Returns the deck, now with its card-order completely shuffled.
    """
    random.shuffle(deck)
    return deck
