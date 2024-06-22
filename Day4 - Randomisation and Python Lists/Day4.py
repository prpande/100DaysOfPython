# Practice 1 - Heads Or Tails

# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲
import random
toss = random.randint(0,1)
if toss == 0:
  print("Heads")
else:
  print("Tails")

##

# Practice 2 - Banker Roulette

names_string = input()
names = names_string.split(", ")
# names_string contains the input values provided. 
# The code above converts the input into an array seperating
# each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random
choice = random.randint(0, len(names) - 1)
print(f"{names[choice]} is going to buy the meal today!")

##

# Practice 3 - Treasure Map

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
column = ord(position[0]) - ord('A')
row = int(position[1]) - 1
map[row][column] = "X"
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")

##

# Project 4 : Rock Paper Scissors

import random

# ASCII art for Rock, Paper, and Scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#Write your code below this line 👇

# List of game images
game_images = [rock, paper, scissors]

# Get user choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

# Ensure user choice is valid
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
else:
    # Print user's choice
    print(game_images[user_choice])

    # Generate computer's choice
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    # Determine the winner
    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif user_choice == computer_choice:
        print("It's a draw")