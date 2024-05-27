# Day 10 - BlackJack Capstone <!-- omit in toc -->

[Online Example](https://www.247blackjack.com/)

[Demo](https://appbrewery.github.io/python-day11-demo/)

- [Overview](#overview)
  - [Introduction to Blackjack](#introduction-to-blackjack)
  - [Basic Rules](#basic-rules)
  - [Example Gameplay](#example-gameplay)
  - [Dealer's Rules](#dealers-rules)
  - [Simplified Game Assumptions](#simplified-game-assumptions)
  - [Project Structure and Resources](#project-structure-and-resources)
  - [Project Guidance](#project-guidance)
- [Hints](#hints)
- [Steps](#steps)

## Overview

### Introduction to Blackjack
- **Objective**: Create a simplified Blackjack game in Python.
- **Game Overview**:
  - **Goal**: Achieve a card total as close to 21 as possible without exceeding it.
  - **Bust**: A hand total exceeding 21 results in an immediate loss.

### Basic Rules
- **Card Values**:
  - **Number Cards (2-10)**: Count as their face value.
  - **Face Cards (Jack, Queen, King)**: Count as 10.
  - **Ace**: Can count as either 1 or 11, chosen to benefit the hand.

### Example Gameplay
- **Initial Deal**:
  - Dealer and player both receive two cards.
  - One of the dealer's cards is hidden.
- **Player's Choices**:
  - Choose to "hit" (receive another card) or "stand" (keep current total).
  - Continue until they either stand or bust.

### Dealer's Rules
- **Revealing Hand**:
  - The dealer reveals their hidden card after the player stands.
- **Dealer's Actions**:
  - Must hit until their total is at least 17.
  - If the dealer busts, the player wins.
  - If both hands are equal, the result is a draw.

### Simplified Game Assumptions
- **Card Representation**:
  - All cards 2-10 included once.
  - Face cards (Jack, Queen, King) each represented as 10.
  - Ace initially counts as 11, switching to 1 if the hand exceeds 21.
- **Infinite Deck**:
  - Cards are not removed from the deck after being dealt, allowing for repeated values.

### Project Structure and Resources
- **Starting Project**:
  - Includes a link to play a version of Blackjack for better understanding.
- **Simplified Rules**:
  - Detailed within the starting file.
- **Difficulty Levels**:
  - Options: Normal, Hard, Extra Hard, Expert.
  - Limitations on hints based on chosen difficulty.

### Project Guidance
- **Step-by-Step Breakdown**:
  - **To-Do List**: Outline the tasks needed to complete the project.
  - **Flowchart**: Visual representation of the game's logic.
  - **Hints**: Provided to assist with different parts of the project, broken into manageable sections.

## Hints

- Go to this website and try out the [Blackjack game](https://games.washingtonpost.com/games/blackjack/)
- Then try out the completed Blackjack project [here](https://appbrewery.github.io/python-day11-demo/) 
- Read [this](http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF) breakdown of program requirements
- Then try to create your own flowchart for the program.
- Download and read [this](https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt) flow chart I've created

## Steps

1. Create a `deal_card()` function that uses the List below to *return* a random card. 11 is the Ace.

    ```python
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    ```

2. Deal the user and computer 2 cards each using `deal_card()` and `append()`.

    ```python
    user_cards = []
    computer_cards = []
    ```

3. Create a function called `calculate_score()` that takes a List of cards as input and returns the score. Look up the `sum()` function to help you do this.

4. Inside `calculate_score()` check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

5. Inside `calculate_score()` check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up `append()` and `remove()`.

6. Call `calculate_score()`. If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

7. If the game has not ended, ask the user if they want to draw another card. If yes, then use the `deal_card()` function to add another card to the `user_cards` List. If no, then the game has ended.

8. The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

9. Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

10. Create a function called `compare()` and pass in the `user_score` and `computer_score`. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the `user_score` is over 21, then the user loses. If the `computer_score` is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

15. Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.