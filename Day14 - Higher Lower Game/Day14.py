# Higher Lower Game Project

from os import name, system
from random import choice

from art import logo, vs
from game_data import data


def clear():
  system('cls' if name == 'nt' else 'clear')

def pick_data(previous_data):
  new_data = previous_data
  while(new_data == previous_data):
    new_data = choice(data)
  return new_data

def display_header(score = 0, is_final = False):
  clear()
  print(logo)
  print("")
  if not is_final:
    if score > 0:
      print(f"You're right! Current score: {score}.")
  else:
    print(f"Sorry, that's wrong. Final score: {score}.")

def ask_question(data_a, data_b):
  print("\n")
  print(f"Compare A: {data_a['name']}, a {data_a['description']}, from {data_a['country']}.")
  print(vs)
  print(f"Against B: {data_b['name']}, a {data_b['description']}, from {data_b['country']}.")
  print("\n")

  answer = input("Who has more followers? Type 'A' or 'B': ").upper()
  if answer == "A":
    return data_a
  else:
    return data_b

def check_answer(answer, data_a, data_b):
  return answer['follower_count'] >= data_a['follower_count'] and answer['follower_count'] >= data_b['follower_count']

def play():
  score = 0
  game_over = False
  data_a = pick_data({})
  data_b = pick_data(data_a)
  while not game_over:
    display_header(score)
    answer = ask_question(data_a, data_b)
    if check_answer(answer, data_a, data_b):
      score += 1
      data_a = data_b
      data_b = pick_data(data_a)
    else:
      game_over = True

  if game_over:
    display_header(score, game_over)

play()
