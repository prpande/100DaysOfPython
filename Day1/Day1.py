# Lesson 1 - Printing

print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")

# Print Modifiers

print("A 'single quote' inside a double quote")
print('A "double quote" inside a single quote')
print("Alternatively you can just \"escape\" the quote")

##

# Lesson 2 - Debugging Practice and String Manipulation

print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

##

# Lesson 3 - Input Function

print(len(input()))

##

## Lesson 4 - VARIABLES

# There are two variables, a and b from input
a = input()
b = input()
# 🚨 Don't change the code above ☝️
####################################
# Write your code below this line 👇
temp = a
a = b
b = temp



# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

##

# Day 1 Project: Band Name Generator

# Welcome message
print("Welcome to the band name generator.")

# Asking user for the city they grew up in
city = input("Which city did you grow up in?\n")

# Asking user for their pet's name
pet = input("What is the name of a pet?\n")

# Generating and displaying the band name
print("Your band name could be " + city + " " + pet)

##