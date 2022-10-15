import random
from copy import deepcopy

"""
Basic strategy trainer for blackjack with multiple decks. All permutations of cards are simulated, with the correct move assigned to each permutation
s = stand
p = split
h = hit
d = double
"""

## card_combos = list(dict.fromkeys(itertools.permutations(["2", "3", "4", "5", "6", "7", "8", "9", "10", "A"], r=2)))

# first two are dealt cards, next is dealer's up card, last is answer
card_combos = [('2', '2', '2', 'h'), ('2', '2', '3', 'h'), ('2', '2', '4', 'p'), ('2', '2', '5', 'p'), ('2', '2', '6', 'p'), ('2', '2', '7', 'p')]


# These hold a list of indexes to the massive card_combos array
correct = []
incorrect = list(range(0, len(card_combos)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]

guessed_incorrectly = []

all_correct = False
while not all_correct:
    # example process for next three lines:
    # incorrect = [0, 1, 6, 9]
    # > index = 2
    # > incorrect_index = 6
    # > cards = ('2', '2', '9')
    index = random.randint(0, len(incorrect) - 1)

    card_combos_index = incorrect[index]  
    cards = card_combos[card_combos_index]

    dealt_cards =  cards[0] + " " + cards[1]
    dealer_face_up = cards[2]
    answer = cards[3]

    while True:
        print("DEALER: ", dealer_face_up)
        print("Dealt: ", dealt_cards)
        guess = input()
        if guess in ['s', 'h', 'd', 'p']:
            break
    if guess == answer:
        correct.append(card_combos_index)
        incorrect.remove(card_combos_index)
        print("CORRECT")
    else:
        # incorrect already holds all the original combos, no need to append
        print("INCORRECT: ", answer)
        if cards not in guessed_incorrectly:
            guessed_incorrectly.append(cards)

    if len(correct) == len(card_combos):
        all_correct = True

print("Finished!")
print("Guessed Incorrectly At Least Once: ", guessed_incorrectly)