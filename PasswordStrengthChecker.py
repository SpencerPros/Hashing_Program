###
## Name: Spencer Prosniewski
## Purpose of Program: Password Strength Checker
###

import re

def check_password_strength(password):
    # Define criteria for a strong password
    length_check = len(password) >= 8  # Check if the password has at least 8 characters
    uppercase_check = re.search(r'[A-Z]', password) is not None  # Check for at least one uppercase letter
    lowercase_check = re.search(r'[a-z]', password) is not None  # Check for at least one lowercase letter
    digit_check = re.search(r'\d', password) is not None  # Check for at least one digit
    special_char_check = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None  # Check for at least one special character

    # Check if all criteria are met
    if all([length_check, uppercase_check, lowercase_check, digit_check, special_char_check]):
        return "Strong Password"
    else:
        return "Weak Password"

# Example usage
# Get the password to check from user input
password_to_check = input("Enter your password: ")

# Call the check_password_strength function with the user-provided password
result = check_password_strength(password_to_check)

# Print the result indicating whether the password is strong or weak
print(result)
