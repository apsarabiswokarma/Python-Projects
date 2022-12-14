# Hint: Take the user choice and then compare it with the computer choice which is taken using the
# random module from a list of choices, and if the user wins then increase the score by 1.


import random
# importing module named random
user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type rock or paper or scissor or Q to quit: ").lower()

    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0,paper:1,scissors:2
    computer_pick = options[random_number]
    print("computer  picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("you won bruh!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("you won bruh!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("you won bruh!")
        user_wins += 1
    else:
        print("you lost bruh!")
        computer_wins += 1

print("you won bruh", user_wins, "times.")
print("computer won bruh", computer_wins, "times.")
print("okay bruh bye!")


# The Goal is to create a command-line game where a user is given a chance to choose
#  between rock, paper, and scissors and if the user wins the score is added,
#  and at the end when the user finishes the game the score is shown to the user.
