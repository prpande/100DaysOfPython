# Practice 1 - Average Height

# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
total_height = 0
number_students = 0
for height in student_heights:
  total_height += height
  number_students+=1

print(f"total height = {total_height}")
print(f"number of students = {number_students}")
print(f"average height = {round(total_height/number_students)}")

##

# Practice 2 - High Score

# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
max = student_scores[0]
for score in student_scores:
  if score > max:
    max = score

print(f"The highest score in the class is: {max}")

##

# Practice 3 - Adding even numbers

target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
sum = 0
for i in  range(2, target + 1, 2):
  sum += i

print(sum)

##

# Practice 4 - Fizzbuzz

# Write your code here 👇
msg = ""
for i in range(1, 101):
  msg = ""
  if i % 3 == 0:
    msg += "Fizz"
  if i % 5 == 0:
    msg += "Buzz"
  if msg == "":
    msg = str(i)
  print(msg)

  ##

  # Project 5: PyPassword Generator

  #Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
for i in range(0, nr_letters):
    password += random.choice(letters)
for i in range(0, nr_symbols):
    password += random.choice(symbols)
for i in range(0, nr_numbers):
    password += random.choice(numbers)

# print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
l = list(password)
random.shuffle(l)
password = ''.join(l)
print(f"Your randomized password is: {password}")
