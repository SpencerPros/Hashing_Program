###
##Name: Spencer Prosniewski
##Purpose of Program: Password Strength Checker
###

import re

def check_password_strength(password):
    # Define criteria for a strong password
    length_check = len(password) >= 8
    uppercase_check = re.search(r'[A-Z]', password) is not None
    lowercase_check = re.search(r'[a-z]', password) is not None
    digit_check = re.search(r'\d', password) is not None
    special_char_check = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Check if all criteria are met
    if all([length_check, uppercase_check, lowercase_check, digit_check, special_char_check]):
        return "Strong Password"
    else:
        return "Weak Password"

# Example usage
password_to_check = input("Enter your password: ")
result = check_password_strength(password_to_check)
print(result)
