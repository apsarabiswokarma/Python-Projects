
# Hint: To generate a number user random number and using a loop gives the user only three\
# chances to guess and according to the user's guess print a satisfactory output.


import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('please type a number larger than 0 next time.')
        quit()

else:
    print("please type a number next time")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0
while True:
    guesses += 1
    user_guess = input("make a guess:")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please type a number next time")
        continue

    if user_guess == random_number:
        print("you got it bruh!")
        break

    elif user_guess > random_number:
        print("you were above the number!")
    else:
        print("you were below the number!")

if guesses >= 2:
    print("You got it in", guesses, "guesses.")

if guesses <= 1:
    print("You got it in", guesses, "guesses.")

print("you got it in bruh", guesses, "guesses")


# In this game, the task is to create a script that generates a random number
# between a range if the user guesses the number right in three chance then user wins otherwise user loss.
