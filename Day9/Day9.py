# Practice 1 - Grading Program

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
  if(student_scores[student] > 90):
    student_grades[student] = "Outstanding"
  elif(student_scores[student] > 80):
    student_grades[student] = "Exceeds Expectations"
  elif(student_scores[student] > 70):
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)

##

# Practice 2 - Dictionary in List

country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 
def add_new_country(country, visits, list_of_cities):
  new_entry = {}
  new_entry["country"] = country
  new_entry["visits"] = visits
  new_entry["cities"] = list_of_cities
  travel_log.append(new_entry)

# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favorite city was {travel_log[2]['cities'][0]}.")

##

# Project 9 - The Secret Auction Program

import os

from art import logo

print(logo)
print("Welcome to the secret auction program.")

done = False
bids = {}
while not done:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  bids[name] = bid
  choice = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  if choice == "no":
    done = True
  os.system('cls' if os.name == 'nt' else 'clear')

max_bid = -1
winner = ""
for name in bids:
  if bids[name] > max_bid:
    max_bid = bids[name]
    winner = name

print(f"The winner is {winner} with a bid of ${max_bid}.")

##
