import string

def is_valid_password(password):
    # Check if the password length is 5
    if len(password) != 5:
        return False                     

    # Check for at least one uppercase letter
    has_uppercase = any(char.isupper() for char in password)
    
    # Check for at least one symbol
    has_symbol = any(char in string.punctuation for char in password)
    
    # The password is valid if it has both an uppercase letter and a symbol
    return has_uppercase and has_symbol
    1
# Get password from the user
password = input("Enter a password: ")

# Validate the password
if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is invalid. It must be exactly 5 characters long, with at least one uppercase letter and one symbol.")