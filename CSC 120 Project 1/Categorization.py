"""
This module will contain the functions related to drawing cards and categorizing them.
"""


def rank_sort(index_one):
    """
    A function that exists to reverse the sorting order of hand of cards.
    When applied, this function will sort the hand by rank, rather than by suit.
    :param: index_one: Parameter generally is named after how the function will be sorting
    entries. This function exists to sort by the first index of a tuple, so its
    parameter is named index_one.
    :return: Returns the first index of an undetermined object.
    """
    return index_one[1]


def draw_hand(deck):
    """
    Draws a hand of 5 cards from the shuffled deck.
    :param: deck: the deck of 52 cards. At this point it is now randomized.
    :return: Returns a hand of 5 random cards from the deck.
    """

    hand = []
    for card in range(5):
        card = deck[0]
        hand.append(card)
        deck.pop(0)
    return hand


def determine_flush(hand):
    """
    A function that categorizes the card hand as a flush.
    :param: hand: A hand of 5 random cards.
    :return: Returns True if the hand is a flush, False otherwise.
    """

    hand.sort()
    suit = hand[0][0]

    for card in hand:
        if card[0] != suit:
            return False
    return True


def determine_pair(hand):
    """
    A function that categorizes the card hand as a pair.
    :param: hand: A hand of 5 random cards.
    :return: Returns True if the hand is a pair, False otherwise.
    """

    hand.sort(key=rank_sort)
    # Sorts in order of rank

    for i in range(0, 4):
        for j in range((i + 1), 5):
            if hand[i][1] == hand[j][1]:
                return True
    return False


def determine_two_pair(hand):
    """
    A function that categorizes the card hand as a two_pair.
    :param: hand: A hand of 5 random cards.
    :return: Returns True if the hand is a two_pair, False otherwise.
    """

    hand.sort(key=rank_sort)
    # Sorts in order of rank

    matching_card_1 = 0
    matching_card_2 = 0
    x = False

    for i in range(0, 4):
        for j in range((i + 1), 5):
            if hand[i][1] == hand[j][1]:
                matching_card_1 = hand[i]
                matching_card_2 = hand[j]
                x = True

    if x:
        hand.remove(matching_card_1)
        hand.remove(matching_card_2)
    else:
        return False

    for i in range(0, 2):
        for j in range((i + 1), 3):
            if hand[i][1] == hand[j][1]:
                hand.append(matching_card_1)
                hand.append(matching_card_2)
                return True

    hand.append(matching_card_1)
    hand.append(matching_card_2)
    return False


def determine_high_card():
    """
    A function that categorizes the card hand as a high_card. This function requires no parameters
    because it will always return True if run.
    :return: Returns True if the hand is a high_card. The return will always be True, because
    every hand that is not a flush,pair, or two_pair must be a high_card.
    """

    return True


def determine_hand(hand):
    """
    This function will determine what category the hand of cards falls into.
    The categories include flushes, pairs, two_pairs, and high_cards.
    :param: hand: A hand of 5 random cards.
    :return: Returns a variable representing a number, the identity of which (1 through 4)
    is important for tabulating data relating to what hands are pulled and how often.
    """

    flush = 0
    pair = 0
    two_pair = 0
    high_card = 0

    if determine_flush(hand):
        flush += 1
        return flush

    if determine_two_pair(hand):
        two_pair += 2
        return two_pair

    if determine_pair(hand):
        pair += 3
        return pair

    if determine_high_card():
        high_card += 4
        return high_card
