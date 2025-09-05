import random
import collections


SUITS = ['Pikes', 'Hearts', 'Tiles', 'Clovers']
VALUES = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']


def create_deck():
    decks = []

    for suit in SUITS:
        for value in VALUES:
            decks.append((suit, value))
    
    return decks


def get_hand(decks, hand_size):
    hand = random.sample(decks, hand_size)
    return hand


def main(hand_size, attempts):
    decks = create_deck()
    hands = []

    for _ in range(attempts):
        hand = get_hand(decks, hand_size)
        hands.append(hand)

    pairs = 0

    for hand in hands:
        values = []

        for deck in hand:
            values.append(deck[1])

        counter = dict(collections.Counter(values))
        
        for value in counter.values():
            if value == 2:
                pairs += 1
                break

    probability_pair = pairs / attempts
    print(f'The probability of get a pair in one hand of {hand_size} decks is {round(probability_pair, 4) * 100}%')

    


if __name__ == '__main__':
    hand_size = int(input('How many decks will there be the hand?: '))
    attempts = int(input('How many attempts do you need to calculate the probabilities?: '))
    
    main(hand_size, attempts)