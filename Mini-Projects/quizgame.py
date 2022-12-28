print("Welcome to my quiz game")

playing = input("Do you want to play? ")

if playing.upper() != "YES":
    quit()

print("okay!let's play the game")

answer = input("what does RAM stands for? ")

if answer.lower() == "random access memory":
    print('Correct answer')
else:
    print("Incorrect!")

answer = input("what does ROM stands for?")

if answer.lower() == "read only memory":
    print('Correct answer')
else:
    print("Incorrect!")

answer = input("what does CPU stands for? ")

if answer.lower() == "central processing unit":
    print('Correct answer')
else:
    print("Incorrect!")

answer = input("what does GUI stands for? ")

if answer.lower() == "graphical user interface":
    print('Correct answer')
else:
    print("Incorrect!")

answer = input("what does URL stands for? ")
if answer.lower() == "uniform resource locator":
    print('Correct answer')

else:
    print("Incorrect!")

answer = input("what does URI stands for? ")
if answer.lower() == "uniform resource identifier":
    print('Correct answer')
else:
    print("Incorrect!")
answer = input("what does NASA stands for? ")
if answer.lower() == " national aeronautics and space administration":
    print('Correct answer')
else:
    print("Incorrect!")
