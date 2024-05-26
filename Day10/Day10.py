# Practice 1 - Days in Month

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  
# TODO: Add more code here 👇
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  days = month_days[month-1]
  if is_leap(year) and month == 2:
    days+= 1
  return days
  
#🚨 Do NOT change any of the code below 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)

##

# Project 10 - Calculator

import os

from art import logo


def add(n1, n2):
  return n1 + n2


def subtract(n1, n2):
  return n1 - n2


def multiply(n1, n2):
  return n1 * n2


def divide(n1, n2):
  return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
opr_string = " "
for operation in operations:
  opr_string += f"{operation} "


def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True

  while should_continue:
    operation_symbol = input(
        f"Pick one of the following operations to perform:{opr_string}: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(
        f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: "
    ) == 'y':
      num1 = answer
    else:
      should_continue = False
      os.system('cls' if os.name == 'nt' else 'clear')
      calculator()


calculator()

##