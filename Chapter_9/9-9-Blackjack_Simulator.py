# 9-9 Blackjack Simulator

# Previously in this chapter you saw the card_dealer.py program that simulates cards being dealt from a deck.
# Enhance the program so it simulates a simplified version fo the game of Blackjack between two virtual players.
# The cards have the following values:
# -Numeric cards are assigned the value they have printed on them. For example, the value of the 2 of spades
# is 2, and the value of the 5 of diamonds is 5.
# -Jacks, queens, and kings are valued at 10.
# -Aces are valued at 1 or 11, depending on the player's choice.
# The program should deal cards to each player until one player's hand is worth more than 21 points.
# When that happens, the other player is the winner.
# (It is possible that both players' hands will simultaneously exceed 21 points, in which case neither player wins.)
# The program should repeat until all the cards have been dealt from the deck.
# If a player id dealt an ace, the program should decide the value of the card according to the following rule:
# The ace will be worth 11 points, unless that makes the players' hand exceed 21 points.
# In that case, the ace will be worth 1 point.
import random

def main():
    # Create a deck of cards.
    deck = create_deck()

    # Deal the cards.
    deal_cards(deck)

# The create_deck function returns a dictionary
# representing a deck of cards.

def create_deck():
    # Create a dictionary with each card and its value
    # stored as key-value pairs.
    deck = {'Ace of Spades':1, '2 of Spades':2, '3 of Spades':3,
            '4 of Spades':4, '5 of Spades':5, '6 of Spades':6,
            '7 of Spades':7, '8 of Spades':8, '9 of Spades':9,
            '10 of Spades':10, 'Jack of Spades':10,
            'Queen of Spades':10, 'King of Spades':10,

            'Ace of Hearts':1, '2 of Hearts':2, '3 of Hearts':3,
            '4 of Hearts':4, '5 of Hearts':5, '6 of Hearts':6,
            '7 of Hearts':7, '8 of Hearts':8, '9 of Hearts':9,
            '10 of Hearts':10, 'Jack of Hearts':10,
            'Queen of Hearts':10, 'King of Hearts':10,

            'Ace of Clubs':1, '2 of Clubs':2, '3 of Clubs':3,
            '4 of Clubs': 4, '5 of Clubs':5, '6 of Clubs':6,
            '7 of Clubs':7, '8 of Clubs':8, '9 of Clubs':9,
            '10 of Clubs':10, 'Jack of Clubs':10,
            'Queen of Clubs':10, 'King of Clubs':10,

            'Ace of Diamonds':1, '2 of Diamonds':2, '3 of Diamonds':3,
            '4 of Diamonds':4, '5 of Diamonds':5, '6 of Diamonds':6,
            '7 of Diamonds':7, '8 of Diamonds':8, '9 of Diamonds':9,
            '10 of Diamonds':10, 'Jack of Diamonds':10,
            'Queen of Diamonds':10, 'King of Diamonds':10}

    # Return the deck.
    return deck

# The deal_cards function deals a specified number of cards
# from the deck.

def deal_cards(deck):
    # Initialize an accumulator for the hand value.
    hand_value1 = 0
    hand_value2 = 0

    # Deal the cards and accumulate their values.
    for count in range(len(deck)//2):
        card1, value1 = random.choice(list(deck.items()))
        print('Player 1 Card: ', card1)
        total_value1 = value1
        del deck[card1]
        if card1.startswith('Ace') and (11 + total_value1) < 21:
            value1 = 11
            total_value1 = value1
        hand_value1 += total_value1
        card2, value2 = random.choice(list(deck.items()))
        print('Player 2 Card: ', card2)
        total_value2 = value2
        del deck[card2]
        if card2.startswith('Ace') and (11 + total_value2) < 21:
            value2 = 11
            total_value2 = value2
        hand_value2 += total_value2
        print(hand_value1, hand_value2)
        if hand_value1 > 21 and hand_value2 <= 21:
            print()
            print('Player 1 is the winner!')
            print()
        elif hand_value2 > 21 and hand_value1 <= 21:
            print()
            print('Player 2 is the winner!')
            print()
        elif hand_value1 > 21 and hand_value2 > 21:
            print()
            print('Neither player wins.')
            print()
        else:
            print()
            print('Round Continues')
            print()
    print('Player 1 Score: ', hand_value1)
    print('Player 2 Score: ', hand_value2)
    if hand_value1 > hand_value2:
        print()
        print('Player 1 Wins!')
    elif hand_value2 > hand_value1:
        print()
        print('Player 2 Wins!')
    else:
        print()
        print('Its a TIE!')

# Call the main function.
main()