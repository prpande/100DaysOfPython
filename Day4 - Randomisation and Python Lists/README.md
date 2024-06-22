# Day 4 - Randomisation and Python Lists<!-- omit in toc -->

- [Lesson 12 - Random Module](#lesson-12---random-module)
  - [Introduction to Randomization](#introduction-to-randomization)
  - [Natural vs. Computer-Generated Randomness](#natural-vs-computer-generated-randomness)
  - [Pseudo-Random Number Generators (PRNGs)](#pseudo-random-number-generators-prngs)
  - [Generating Random Numbers in Python](#generating-random-numbers-in-python)
    - [Generating Random Integers](#generating-random-integers)
    - [Generating Random Floating-Point Numbers](#generating-random-floating-point-numbers)
  - [Modules in Python](#modules-in-python)
  - [Applications of Random Numbers](#applications-of-random-numbers)
    - [Example: Love Score Calculator](#example-love-score-calculator)
- [Practice 1 - Heads Or Tails](#practice-1---heads-or-tails)
- [Lesson 13 -  Understanding the Offset and Appending Items to Lists](#lesson-13----understanding-the-offset-and-appending-items-to-lists)
  - [Introduction to Lists](#introduction-to-lists)
  - [Basic Operations](#basic-operations)
  - [Accessing List Elements](#accessing-list-elements)
  - [Modifying Lists](#modifying-lists)
  - [List Functions](#list-functions)
  - [Indexing Peculiarities](#indexing-peculiarities)
  - [Documentation and Learning](#documentation-and-learning)
- [Practice 2 - Banker Roulette](#practice-2---banker-roulette)
- [Lesson 14 - IndexErrors and Working with Nested Lists](#lesson-14---indexerrors-and-working-with-nested-lists)
  - [Common Errors with Lists](#common-errors-with-lists)
    - [Index Out of Range Error](#index-out-of-range-error)
    - [Off-by-One Error](#off-by-one-error)
  - [Nested Lists](#nested-lists)
    - [Example: Creating Nested Lists](#example-creating-nested-lists)
  - [Accessing Elements in Nested Lists](#accessing-elements-in-nested-lists)
  - [Practical Tips](#practical-tips)
- [Practice 3 - Treasure Map](#practice-3---treasure-map)
- [Project 4 : Rock Paper Scissors](#project-4--rock-paper-scissors)


## Lesson 12 - Random Module

### Introduction to Randomization
- **Importance of Randomization**: 
  - Essential for creating unpredictability in computer programs.
  - Commonly used in games to make them engaging (e.g., unpredictable Tetris blocks).

### Natural vs. Computer-Generated Randomness
- **Natural Randomness**: Easily observed in daily life (e.g., splashing paint, TV static).
- **Computers and Determinism**: Computers operate deterministically (repeatable, predictable actions).

### Pseudo-Random Number Generators (PRNGs)
- **Definition**: Algorithms used to generate sequences of numbers that approximate true randomness.
- **Python's PRNG**: Uses the [Mersenne Twister](https://en.wikipedia.org/wiki/Mersenne_Twister) algorithm.
  - For detailed algorithmic understanding, refer to resources like [Wikipedia](https://en.wikipedia.org/wiki/Mersenne_Twister) or [Khan Academy](https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/random-vs-pseudorandom-number-generators).

### Generating Random Numbers in Python
- **Python's Random Module**: 
  - Provides functions to generate random integers and floating-point numbers.
  - Accessible through importing the module: `import random`.

#### Generating Random Integers
- **Function**: `random.randint(a, b)`
  - Generates a random integer between `a` and `b` (inclusive).
- **Example**:
  ```python
  import random
  random_int = random.randint(1, 10)
  print(random_int)
  ```

#### Generating Random Floating-Point Numbers
- **Function**: `random.random()`
  - Generates a random float between 0 (inclusive) and 1 (exclusive).
- **Example**:
  ```python
  random_float = random.random()
  print(random_float)
  ```

- **Scaling Random Floats**: 
  - To generate a random float between 0 and `n`: multiply the result of `random.random()` by `n`.
  - Example for range 0 to 5:
    ```python
    random_float = random.random() * 5
    print(random_float)
    ```

### Modules in Python
- **Definition**: Reusable pieces of code (functions, variables) stored in separate files.
- **Importing Modules**: Allows code to be split for better organization and collaboration.
- **Creating a Module**:
  - Create a new file (e.g., `my_module.py`).
  - Define functions or variables inside this file.
  - Import the module in your main code file:
    ```python
    import my_module
    print(my_module.pi)
    ```

### Applications of Random Numbers
- **Random Number-Based Applications**:
  - Love calculator (previous lesson).
  - Dice rolls, coin flips, random selections in games.

#### Example: Love Score Calculator
- **Using Random Integers**:
  ```python
  love_score = random.randint(1, 100)
  print(f"Your love score is {love_score}")
  ```

## Practice 1 - Heads Or Tails

You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

Important, the first letter should be capitalised and spelt exactly like in the example e.g. "Heads", **not** "heads".

There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out "Heads" or "Tails".

e.g. 1 means Heads 0 means Tails

**Example Output**

```
Heads
```

or

```
Tails
```

## Lesson 13 -  Understanding the Offset and Appending Items to Lists

### Introduction to Lists
- **Definition**: A list is a data structure in Python that allows you to store and organize multiple pieces of data.
- **Purpose**: Useful for storing grouped or related data, such as names of states in the US or items in a queue.
- **Syntax**: Lists are defined using square brackets `[]`, with items separated by commas.

### Basic Operations
1. **Creating a List**
   - Example: `fruits = ["Cherry", "Apple", "Pear"]`
   - Mixed data types are allowed: `mixed_list = [1, "hello", True]`

2. **Storing Data in Lists**
   - Instead of multiple variables for related data, use a list:
     ```python
     states_of_america = ["Delaware", "Pennsylvania", "New Jersey", ...]
     ```

3. **List Order**
   - Lists maintain the order of elements. The position of items matters, especially for ordered data like states joining the union.

### Accessing List Elements
- **Indexing**: Use square brackets with an index to access elements.
  - Positive indices start from 0.
    - Example: `states_of_america[0]` returns "Delaware".
  - Negative indices start from -1 (last element).
    - Example: `states_of_america[-1]` returns the last state in the list.

### Modifying Lists
1. **Changing Elements**
   - Example: Change "Pennsylvania" to "Pencilvania":
     ```python
     states_of_america[1] = "Pencilvania"
     ```

2. **Appending Elements**
   - Adding an item to the end of the list:
     ```python
     states_of_america.append("Angelaland")
     ```

3. **Extending Lists**
   - Adding multiple items at once:
     ```python
     new_states = ["NewState1", "NewState2"]
     states_of_america.extend(new_states)
     ```

### List Functions
- Python lists come with several built-in functions (methods) to manipulate the list data.
  - **Append**: Adds a single element to the end.
  - **Extend**: Adds multiple elements from another list.

### Indexing Peculiarities
- **0-based Indexing**: Python (and many other programming languages) uses 0-based indexing.
  - First element has index 0.
  - Index represents the offset from the start.

### Documentation and Learning
- **Documentation**: Python’s official documentation provides detailed information on all list methods.
- **Practical Learning**: Rather than memorizing all methods, familiarize yourself with what is possible and use documentation/Google as needed.
- **Programming Practice**: Think of programming as an open-book exam where knowing how to find and use information is key.

## Practice 2 - Banker Roulette

You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

**Important**: You are not allowed to use the `choice()` function.

Line 1 splits the string `names_string` into individual names and puts them inside a List called names. For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name

HINT: Assume that names looks like this: input: x, y, z, names = ["x", "y", "z"]

**Example Input**
```
Angela, Ben, Jenny, Michael, Chloe
```

Note: notice that there is a space between the comma and the next name.

**Example Output**
```
Michael is going to buy the meal today!
```

**Hints**
- You might need the help of the len() function. https://stackoverflow.com/questions/1712227/how-do-i-get-the-number-of-elements-in-a-list
- Remember that Lists start at index 0!

## Lesson 14 - IndexErrors and Working with Nested Lists

### Common Errors with Lists

#### Index Out of Range Error
- **Definition**: This error occurs when you try to access an index that does not exist in the list.
- **Example**:
  ```python
  states_of_america = ["Delaware", "Pennsylvania", "New Jersey", ...]  # 50 states
  print(len(states_of_america))  # Prints 50
  print(states_of_america[49])  # Prints "Hawaii"
  print(states_of_america[50])  # IndexError: list index out of range
  ```

- **Cause**: This happens when the index used is beyond the range of the list. Since Python lists are 0-indexed, the valid indices for a list of length 50 are 0 to 49.

#### Off-by-One Error
- **Definition**: A common error where the index used is off by one, usually when iterating through lists or accessing elements based on list length.
- **Example**:
  ```python
  num_of_states = len(states_of_america)  # num_of_states is 50
  print(states_of_america[num_of_states])  # IndexError: list index out of range
  ```

- **Solution**: Adjust the index by subtracting 1 to fit the valid range:
  ```python
  print(states_of_america[num_of_states - 1])  # Correctly prints the last state
  ```

### Nested Lists
- **Definition**: A nested list is a list that contains other lists as its elements.
- **Use Case**: Useful for organizing related data within a single structure.

#### Example: Creating Nested Lists
- **Scenario**: Creating a list of the "Dirty Dozen" fruits and vegetables with high pesticide levels.
  ```python
  fruits = ["Strawberries", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
  vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
  dirty_dozen = [fruits, vegetables]
  print(dirty_dozen)
  ```

- **Output**:
  ```
  [["Strawberries", "Apples", "Grapes", "Peaches", "Cherries", "Pears"], ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]]
  ```

### Accessing Elements in Nested Lists
- **Accessing Sub-Lists**: Use the primary index to access the sub-list.
  ```python
  print(dirty_dozen[0])  # Prints the fruits list
  print(dirty_dozen[1])  # Prints the vegetables list
  ```

- **Accessing Elements within Sub-Lists**: Chain the indices.
  ```python
  print(dirty_dozen[0][1])  # Prints "Apples" from the fruits list
  print(dirty_dozen[1][2])  # Prints "Tomatoes" from the vegetables list
  ```

### Practical Tips
- **Avoiding Index Errors**: Always ensure your indices are within the valid range by checking list lengths.
- **Using Nested Lists**: Ideal for grouping related data, providing flexibility and structure to your programs.
- **Documentation**: Utilize Python's official documentation to explore more list methods and practices.

## Practice 3 - Treasure Map

This is a difficult challenge. 💪

You are going to write a program that will mark a spot on a map with an X.

In the starting code, you will find a variable called map.

This map contains a nested list. When map is printed this is what it looks like, notice the nesting:

[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

This is a bit hard to work with. So on lines 6 and 23, we've used this line of code print(f"{row1}\n{row2}\n{row3}") to format the 3 lists to be printed as a 3 by 3 grid, each on a new line.

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

Now it looks a bit more like the coordinates of a real map:

Your job is to write a program that allows you to mark a square on the map using a letter-number system.

So an input of A3 should place an X at the position shown below:


First, your program must take the user input and convert it to a usable format.

Next, you need to use that input to update your nested list with an "X". Remember that your nested list map actually looks like this:

[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

**Example Input 1**
```
B3
```
**Example Output 1**
```
Hiding your treasure! X marks the spot.
['⬜️', '️⬜️', '️⬜️']
['⬜️', '⬜️', '️⬜️']
['⬜️️', 'X', '⬜️️']
```
**Example Input 2**
```
B1
```
***Example Output 2***
```
Hiding your treasure! X marks the spot.
['⬜️', 'X', '️⬜️']
['⬜️', '⬜️', '️⬜️']
['⬜️️', '⬜️️', '⬜️️']
```

**Hints**
- See if this List method helps you: https://www.w3schools.com/python/ref_list_index.asp
- Remember that nested Lists in Python are accessed from outside to inside. e.g. In the List below:

list = [['A', 'B, 'C'], 'E', 'F', 'G']

E is list[1] C is list[0][2]

Check your formatting. This is correctly formatted:
```
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', 'X', '⬜️']
```
vs.

Incorrectly formatted (missing a space before 'X and extra space after the X and extra space before the comma):
```
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️','X ' , '⬜️']
```

## Project 4 : Rock Paper Scissors

**Objective:**
Develop a Rock Paper Scissors game where a user can play against the computer. The game will prompt the user to input their choice and will then randomly generate a choice for the computer. The game will compare the choices and determine the winner based on the traditional rules of Rock Paper Scissors.

**Requirements:**
1. **User Input:**
   - The game should prompt the user to type `0` for Rock, `1` for Paper, or `2` for Scissors.
   
2. **Computer Choice:**
   - The game should randomly generate a number between `0` and `2` to represent the computer's choice of Rock, Paper, or Scissors.

3. **Game Logic:**
   - Compare the user’s choice with the computer’s choice to determine the outcome.
   - Use the rules:
     - Rock (0) beats Scissors (2)
     - Scissors (2) beats Paper (1)
     - Paper (1) beats Rock (0)
   - If both choices are the same, it’s a draw.

4. **Output:**
   - Display the user’s choice and the computer’s choice using ASCII art representations.
   - Print the result of the game: whether the user wins, loses, or it’s a draw.
   - Handle invalid inputs by informing the user and ending the game.

5. **Error Handling:**
   - Ensure that the game handles cases where the user inputs a number outside the range of `0`, `1`, or `2`.
   - If an invalid input is detected, the game should print a message indicating that the input was invalid and that the user loses.

**Steps to Implement:**
1. **Setup the Game Environment:**
   - Create a Python script and import necessary modules (e.g., `random` for generating computer choices).

2. **Define Variables:**
   - Create variables to store the ASCII art for Rock, Paper, and Scissors.
   - Create a list to hold these ASCII art variables.

3. **Prompt User for Input:**
   - Use the `input` function to get the user’s choice and convert it to an integer.

4. **Generate Computer Choice:**
   - Use the `random.randint` function to generate a random choice for the computer between `0` and `2`.

5. **Display Choices:**
   - Print the ASCII art corresponding to the user’s and computer’s choices.

6. **Implement Game Logic:**
   - Use if-elif-else statements to determine the winner based on the game rules.
   - Include checks for draw situations and invalid inputs.

7. **Test the Game:**
   - Run the game multiple times to ensure it correctly handles all possible inputs and outputs the correct results.


**Additional Notes:**
- Encourage the use of flow diagrams to map out the game logic before coding.
- Testing the game frequently during development will help catch bugs early.
- Encourage students to explore adding enhancements such as keeping score, adding more rounds, or providing a user-friendly interface.

[Demo](https://appbrewery.github.io/python-day4-demo/)