'''
Name: Spencer Prosniewski
Date: 10/8/2023
Purpose: Homework 2 (make a program to convert meters to feet, and find the area of a triangle)
'''

# Task 1: Read a number in feet, convert it to meters, and display the result.
feet_input = input("Enter a length in feet: ")
feet = eval(feet_input)
meters = feet * 0.305
print(f"{feet} feet is equal to {meters} meters.")

# Task 2: Read the base and height of a triangle, calculate its area, and display the result.
base_input = input("Enter the base of the triangle: ")
height_input = input("Enter the height of the triangle: ")
base = eval(base_input)
height = eval(height_input)
area = 0.5 * base * height
print(f"The area {area} square units.")


