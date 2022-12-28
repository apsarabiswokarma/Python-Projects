name = input("type your name bruh:")
print("WELCOME", name, "to this wonderful adventure!")

answer = input(
    'you are on dirt road,it has come to an end.you can go left or right. \
    which direction would you like to go? ').lower()

if answer == "left":
    answer = input(
        "you come to a deep river bruh,you can walk around it or swim across? \
        Type walk to walk around and swim to swim across:").lower()
    if answer == "swim":
        print("you swam across and were eaten by crocodile.So RIP bruh.")
    elif answer == "walk":
        print("you walk for many miles bruh .DO you want to drink water bruh?\
        kidding ran out of water and you loss the game")
    else:
        print("not a valid option you lose.")
elif answer == "right":
    answer = input(
        "you come to a bridge ,it loons wobbly,\
            do you want to cross it or head back(cross or back)? ")
    if answer == "back":
        print("you go back and lose bruh.")
    elif answer == "cross":
        answer = input("you cross the bridge and meet the beautiful girl Apsara.\
            Do you want to talk with her?(yes/no?)").lower()
    if answer == "yes":
        print("you talk to her ans she gives you diamond.YOU WIN BRUH CONGRATULATION!! ")
    if answer == "no":
        print("you ignore her and she slaps you SO you lose bruh.")
    else:
        print("not a valid option bruh. YOU lose.")

print("thank you for trying dear", name)
