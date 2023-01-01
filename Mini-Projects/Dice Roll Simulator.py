import random


def roll_dice():
    dice_roll = random.randint(1, 6)
    print(f"You rolled a {dice_roll}")


# roll the dice 10 times
for i in range(10):
    roll_dice()

# This code defines a function called roll_dice that generates a random number between 1 and 6 (inclusive) using the random.
# randint function. It then prints a message indicating the roll.
# To roll the dice 10 times, we use a for loop to call the roll_dice function 10 times.
# This will print 10 messages indicating the result of each dice roll.
