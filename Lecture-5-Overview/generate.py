import random # Gives access to all functions within that specific module

coin = random.choice(["heads", "tails"])
print(coin)

# OR

from random import choice # from {module} import {specific function}

coin = choice(["heads", "tails"])
print(coin)

# OR

import random

number = random.randint(1, 10) # Generates random number, 10% probability each
print(number)

# OR

import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)

for card in cards:
    print(card) # Prints card by card on new line