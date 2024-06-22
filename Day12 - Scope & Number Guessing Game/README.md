# Day 12 - Scope & Number Guessing Game<!-- omit in toc -->

- [Lesson 25 - Namespaces: Local vs. Global Scope](#lesson-25---namespaces-local-vs-global-scope)
  - [Concept of Scope](#concept-of-scope)
  - [Local Scope](#local-scope)
  - [Global Scope](#global-scope)
  - [Differences Between Local and Global Scope](#differences-between-local-and-global-scope)
  - [Practical Example with Functions](#practical-example-with-functions)
  - [Namespace](#namespace)
  - [Summary](#summary)
- [Lesson 26 - Does Python Have Block Scope?](#lesson-26---does-python-have-block-scope)
  - [No Block Scope in Python](#no-block-scope-in-python)
  - [Example of No Block Scope](#example-of-no-block-scope)
  - [Local Scope within Functions](#local-scope-within-functions)
  - [Key Points to Remember](#key-points-to-remember)
  - [Practical Implications](#practical-implications)
- [Lesson 27 - How to Modify a Global Variable](#lesson-27---how-to-modify-a-global-variable)
  - [Understanding Global Scope](#understanding-global-scope)
  - [Example of Scope in Practice](#example-of-scope-in-practice)
  - [Modifying Global Variables within a Function](#modifying-global-variables-within-a-function)
  - [Why Avoid Modifying Global Scope](#why-avoid-modifying-global-scope)
  - [Using Return Statements to Avoid Modifying Global Scope](#using-return-statements-to-avoid-modifying-global-scope)
  - [Key Points to Remember](#key-points-to-remember-1)
  - [Practical Example of Proper Scope Usage](#practical-example-of-proper-scope-usage)
- [Lesson 28 - Python Constants and Global Scope](#lesson-28---python-constants-and-global-scope)
  - [Careful Use of Global Scope](#careful-use-of-global-scope)
  - [Benefits of Global Scope](#benefits-of-global-scope)
  - [Naming Conventions for Global Constants](#naming-conventions-for-global-constants)
  - [Using Global Constants](#using-global-constants)
  - [Recap of Scope Concepts](#recap-of-scope-concepts)
  - [Summary](#summary-1)
- [Project 12 - The Number Guessing Game](#project-12---the-number-guessing-game)
  - [Overview](#overview)
  - [Requirements](#requirements)
  - [Steps to Develop the Project](#steps-to-develop-the-project)
  - [Notes](#notes)


## Lesson 25 - Namespaces: Local vs. Global Scope

### Concept of Scope
- Scope defines the accessibility of variables and functions in different parts of a program.
- It can be visualized as a house with a fenced garden (local scope) versus an apple tree in the neighborhood (global scope).

### Local Scope
- Variables created inside a function are only accessible within that function.
- Example: 
  ```python
  def drink_potion():
      potion_strength = 2
      print(potion_strength)  # Accessible within the function

  drink_potion()  # Outputs: 2
  print(potion_strength)  # Error: potion_strength is not defined
  ```
- Variables defined inside a function have local scope and cannot be accessed outside the function.

### Global Scope
- Variables created outside any function are accessible throughout the file, both inside and outside functions.
- Example:
  ```python
  player_health = 10

  def drink_potion():
      potion_strength = 2
      print(player_health)  # Accessible within the function

  drink_potion()  # Outputs: 10
  print(player_health)  # Outputs: 10
  ```
- Variables defined at the top level of the file (not within any function) have global scope.

### Differences Between Local and Global Scope
- Local scope is confined to the function where the variable is defined.
- Global scope extends across the entire file, making the variable accessible everywhere.

### Practical Example with Functions
- Consider the following code:
  ```python
  enemies = 1

  def increase_enemies():
      enemies = 2
      print(f"enemies inside function: {enemies}")

  increase_enemies()  # Outputs: enemies inside function: 2
  print(f"enemies outside function: {enemies}")  # Outputs: enemies outside function: 1
  ```
  - Inside the function `increase_enemies`, `enemies` is set to 2, but this does not affect the global variable `enemies`.
  - Outside the function, `enemies` remains 1 because the assignment inside the function is in a different scope.

### Namespace
- Namespace refers to the context where a variable or function is defined and determines its scope.
- Every named entity (variables, functions) has a namespace that is valid in specific scopes.
- Example:
  ```python
  def game():
      def drink_potion():
          potion_strength = 2
      drink_potion()

  game()  # drink_potion is called within game
  drink_potion()  # Error: drink_potion is not defined
  ```
  - `drink_potion` is defined within the `game` function, so it has local scope within `game`.

### Summary
- Scope is crucial for understanding variable and function accessibility within a program.
- Local scope limits accessibility to within the function where the variable is defined.
- Global scope allows accessibility throughout the entire file.
- Proper understanding of scope and namespaces helps in writing clearer and bug-free code.

## Lesson 26 - Does Python Have Block Scope?

### No Block Scope in Python
- Unlike some other programming languages such as C++ or Java, Python does not have block scope.
- Variables created inside blocks (if, while, for) do not have separate scope from their enclosing functions or global scope if not enclosed by a function.

### Example of No Block Scope
- Consider the following code:
  ```python
  enemies = ["skeleton", "zombie", "alien"]
  game_level = 3

  if game_level < 5:
      new_enemy = enemies[0]

  print(new_enemy)  # Outputs: skeleton
  ```
  - The variable `new_enemy` is created within an if block.
  - Despite the if block, `new_enemy` has the same scope as its enclosing function or global scope.
  - Thus, `new_enemy` is accessible outside the if block and prints "skeleton".

### Local Scope within Functions
- When variables are created inside a function, they have local scope and are not accessible outside the function.
- Example:
  ```python
  def create_enemy():
      if game_level < 5:
          new_enemy = enemies[0]
      print(new_enemy)  # This line is within the function

  create_enemy()  # Outputs: skeleton
  print(new_enemy)  # Error: new_enemy is not defined
  ```
  - `new_enemy` is accessible anywhere within the `create_enemy` function.
  - Trying to access `new_enemy` outside the function results in an error.

### Key Points to Remember
- **Global Scope**: Variables defined outside any function are accessible throughout the file.
- **Local Scope**: Variables defined inside a function are only accessible within that function.
- **No Block Scope**: Blocks of code like if, while, for do not create a new scope in Python. Variables defined within these blocks have the same scope as the surrounding code.

### Practical Implications
- Ensure awareness of where variables are defined to avoid scope-related errors.
- Understand that indentation and colons (used in blocks like if, while, for) do not create separate local scopes.
- Functions create a clear boundary for variable scope, restricting access to variables outside the function.

## Lesson 27 - How to Modify a Global Variable

### Understanding Global Scope
- **Global Variables**: Variables defined outside any function and accessible throughout the file.
- **Local Variables**: Variables defined within a function, accessible only within that function.

### Example of Scope in Practice
- Consider the following code:
  ```python
  enemies = "skeleton"

  def increase_enemies():
      enemies = "zombie"
      print(f"Enemies inside function: {enemies}")

  increase_enemies()  # Outputs: Enemies inside function: zombie
  print(f"Enemies outside function: {enemies}")  # Outputs: Enemies outside function: skeleton
  ```
  - The `enemies` variable inside the function creates a new local variable, separate from the global `enemies`.

### Modifying Global Variables within a Function
- To modify a global variable within a function, you must explicitly declare it as global using the `global` keyword.
- Example:
  ```python
  enemies = 1

  def increase_enemies():
      global enemies
      enemies += 1

  increase_enemies()
  print(enemies)  # Outputs: 2
  ```
  - The `global` keyword allows the function to modify the global `enemies` variable.

### Why Avoid Modifying Global Scope
- Modifying global variables within functions can lead to confusion and bugs because:
  - The global variable can be defined anywhere in the code.
  - Modifications are independent of the variable’s creation point.
  - It can make the code harder to debug and maintain.

### Using Return Statements to Avoid Modifying Global Scope
- Instead of modifying a global variable within a function, use return statements to return the new value and assign it outside the function.
- Example:
  ```python
  enemies = 1

  def increase_enemies(enemies):
      return enemies + 1

  enemies = increase_enemies(enemies)
  print(enemies)  # Outputs: 2
  ```
  - The function returns the modified value, which is then assigned to the global variable outside the function.

### Key Points to Remember
- **Global Scope**: Variables defined globally can be accessed but should be modified with caution within functions.
- **Local Scope**: Variables defined within functions should be used for operations to maintain code clarity and reduce errors.
- **Global Keyword**: Use `global` to modify global variables within a function.
- **Return Statements**: Prefer returning modified values from functions and assigning them outside the function to avoid modifying global scope directly.

### Practical Example of Proper Scope Usage
- Example of avoiding direct modification of a global variable:
  ```python
  enemies = 1

  def increase_enemies(enemies):
      return enemies + 1

  enemies = increase_enemies(enemies)
  print(enemies)  # Outputs: 2
  ```
  - This approach keeps the function self-contained and avoids potential bugs associated with modifying global variables directly.

## Lesson 28 - Python Constants and Global Scope

### Careful Use of Global Scope
- **Global Scope**: Variables defined globally and accessible throughout the program.
- **Caution with Global Variables**: Modifying global variables within functions can lead to confusion and bugs. However, global scope is not to be avoided entirely.

### Benefits of Global Scope
- **Global Constants**: Useful for defining values that are never intended to change, such as mathematical constants or configuration settings.
- **Example of a Global Constant**:
  ```python
  PI = 3.14159
  BASE_URL = "https://api.example.com"
  ```

### Naming Conventions for Global Constants
- **Uppercase Naming**: To differentiate constants from variables that may change, global constants are named using all uppercase letters with underscores.
  - Example: 
    ```python
    PI = 3.14159
    TWITTER_HANDLE = "@example"
    ```

### Using Global Constants
- **Accessing Constants**: When you need to use a global constant inside a function, you can access it directly, reminding you not to modify it.
  - Example:
    ```python
    def calculate_circumference(radius):
        return 2 * PI * radius

    print(calculate_circumference(5))  # Outputs: 31.4159
    ```

### Recap of Scope Concepts
- **Global Scope**: Variables defined outside any function, accessible throughout the program.
- **Local Scope**: Variables defined within a function, accessible only within that function.
- **Global Constants**: Use uppercase naming to signify that these values should not be modified.
- **Best Practices**: Avoid modifying global variables within functions; use return statements to handle changes.

### Summary
- Global scope is useful, especially for constants.
- Use naming conventions to distinguish between constants and variables.
- Access global constants within functions without modifying them.
- Practice careful and thoughtful use of global variables to maintain code clarity and prevent bugs.

## Project 12 - The Number Guessing Game

[Demo](https://appbrewery.github.io/python-day12-demo/)

### Overview
Create a number guessing game where the player attempts to guess a number between 1 and 100. The game provides feedback on whether the guessed number is too high or too low. The game has two difficulty levels: easy and hard.

### Requirements
1. **Game Initialization**:
   - Welcome message. [ASCII Art](http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20)
   - Prompt for difficulty level (easy or hard).

2. **Gameplay Mechanics**:
   - Randomly select a number between 1 and 100.
   - Provide feedback on whether the guess is too high or too low.
   - Track the number of attempts.
   - Different attempt limits based on difficulty:
     - Easy: 10 attempts.
     - Hard: 5 attempts.
   - Declare a win if the player guesses correctly within the allowed attempts.
   - Declare a loss if the player runs out of attempts without guessing correctly.

3. **User Interaction**:
   - Input for difficulty level selection.
   - Input for each guess.
   - Feedback on guess (too high, too low).
   - Display remaining attempts after each guess.
   - Final message indicating win or loss.

4. **Replayability**:
   - Option to replay the game after a win or loss.

5. **Additional Features**:
   - ASCII art for the game title.
   - Ability to customize the game's visual appearance (e.g., ASCII art).

### Steps to Develop the Project
1. **Understand the Game**:
   - Play the game multiple times to familiarize yourself with its mechanics and flow.

2. **Break Down the Problem**:
   - Create a detailed to-do list of tasks to implement the game.
   - Identify key functionalities and their respective requirements.

3. **Design the Program**:
   - Outline the structure of your program, including functions and variables.
   - Plan the user interface and interactions.

4. **Implementation**:
   - Start coding based on your design.
   - Add comments to explain the functionality of each part of the code.

5. **Testing**:
   - Test the game thoroughly to ensure it works correctly under all scenarios.
   - Check for edge cases and handle potential errors.

6. **Enhancements**:
   - Add optional features such as custom ASCII art for the game title.
   - Ensure the game's visual elements are correctly displayed.

### Notes
- You have full creative freedom in terms of styling and wording.
- Use external resources for ASCII art and incorporate them into your project as needed.
- The final project must retain the core functionality as described above.