
# Hint: Divide the email into two strings using @ as divider

def slice_email(email):
    username = email[:email.index("@")]
    domain = email[email.index("@")+1:]
    return username, domain


# test the function
email = "john.doe@example.com"
username, domain = slice_email(email)
print(f"Username: {username}\nDomain: {domain}")

# This code defines a function called slice_email that takes an email address \
#  as an argument and returns the username and domain as a tuple.
#  It uses the index method to find the position of the @ symbol, and then slices the email address using this position.
# To test the function, we call it with an email address and print the resulting username and domain.
