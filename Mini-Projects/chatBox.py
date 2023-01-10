# Here's an example of a simple command-line chat program written in Python:

print("Welcome to the chat program!")
username = input("Please enter your username: ")
print("Hello, " + username + "! You can start typing to chat.")
while True:
    message = input(username + ": ")
    if message.strip().lower() == "exit":
        print("Exiting chat...")
        break
    else:
        print("Other User: " + message)

# This code will first display a welcome message, then prompt the user to enter their username.
#  The program then enters a infinite loop that will take input from
# the user and print it, until the user types "exit" to exit the chat.
