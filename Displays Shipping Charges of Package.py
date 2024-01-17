'''
Name: Spencer Prosniewski
Date: 10/13/2023
Purpose: (Hw 3) Write a program that displays shipping charges of a package
'''

# Input the weight of the package using eval
weight = eval(input("Enter the weight of the package in pounds: "))

# Determine the shipping cost based on the weight
if weight <= 2:
    cost_per_pound = 1.10
elif weight <= 6:
    cost_per_pound = 2.20
elif weight <= 10:
    cost_per_pound = 3.70
else:
    cost_per_pound = 3.80

# Calculate shipping charges
shipping_charges = weight * cost_per_pound

# Display the company name, shipping charges, and total charges
company_name = "Fast Freight Shipping Company."
print("\nCompany Name: ", company_name)
print("Weight of the package: ", weight, " pounds")
print("Shipping charges: $", shipping_charges)



