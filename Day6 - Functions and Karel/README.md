# Day 6 - Python Functions & Karel<!-- omit in toc -->

- [Lesson 17 - Defining and Calling Python Functions](#lesson-17---defining-and-calling-python-functions)
  - [What are Functions?](#what-are-functions)
  - [Built-in Functions](#built-in-functions)
  - [Using Functions in Python](#using-functions-in-python)
  - [Creating User-Defined Functions](#creating-user-defined-functions)
  - [Executing (Calling) Functions](#executing-calling-functions)
  - [Example: Reeborg's World (Robot Programming)](#example-reeborgs-world-robot-programming)
  - [Creating Custom Commands with Functions](#creating-custom-commands-with-functions)
  - [Function Example: Creating `turn_right`](#function-example-creating-turn_right)
  - [Exercise: Drawing a Square with the Robot](#exercise-drawing-a-square-with-the-robot)
  - [Benefits of Using Functions](#benefits-of-using-functions)
  - [Summary](#summary)
- [Practice 1 - Reeborg Hurdle Jumping Challenge](#practice-1---reeborg-hurdle-jumping-challenge)
- [Lesson 18 - Indentation](#lesson-18---indentation)
  - [Importance of Indentation in Python](#importance-of-indentation-in-python)
  - [Indentation Basics](#indentation-basics)
  - [Visualizing Indentation](#visualizing-indentation)
  - [Indentation with Other Structures](#indentation-with-other-structures)
  - [Nested Blocks](#nested-blocks)
  - [Spaces vs. Tabs Debate](#spaces-vs-tabs-debate)
  - [Using Code Editors for Indentation](#using-code-editors-for-indentation)
  - [Example of Configuring a Code Editor](#example-of-configuring-a-code-editor)
  - [Summary](#summary-1)
- [Lesson 19 - While Loops](#lesson-19---while-loops)
  - [Introduction to While Loops](#introduction-to-while-loops)
  - [Syntax of While Loops](#syntax-of-while-loops)
  - [Example: Simple Robot with While Loop](#example-simple-robot-with-while-loop)
  - [Using While Loops in Practice](#using-while-loops-in-practice)
  - [Explanation of Code Execution](#explanation-of-code-execution)
  - [Handling Dynamic Conditions](#handling-dynamic-conditions)
  - [Important Concepts](#important-concepts)
  - [Choosing Between For and While Loops](#choosing-between-for-and-while-loops)
  - [Dangers of While Loops: Infinite Loops](#dangers-of-while-loops-infinite-loops)
  - [Example: Debugging Infinite Loops](#example-debugging-infinite-loops)
  - [Conclusion](#conclusion)
- [Practice 2 - Reeborg's Hurdles 3 Challenge using While Loops](#practice-2---reeborgs-hurdles-3-challenge-using-while-loops)
- [Practice 3 - Reeborg's Hurdles 4 Challenge with variable heights](#practice-3---reeborgs-hurdles-4-challenge-with-variable-heights)
- [Project 6  - Reebog's Escaping the Maze](#project-6----reebogs-escaping-the-maze)



## Lesson 17 - Defining and Calling Python Functions

### What are Functions?
- Functions are blocks of code designed to perform specific tasks.
- Analogous to human roles (e.g., mother, father, son, daughter) where each role has specific functions.
- Functions help us organize and reuse code.

### Built-in Functions
- **`len()`**: Returns the number of items in a collection.
- **`int()`**: Converts a value to an integer.
- **`print()`**: Outputs text to the console.
- **`range()`**: Generates a sequence of numbers.
- Python has many built-in functions, all of which are documented in the Python documentation.

### Using Functions in Python
- A function call consists of the function's name followed by parentheses `()`.
  - Example: `print("Hello")` outputs "Hello" to the console.
  - Example: `len("Hello")` returns 5.
- Functions can be used with variables:
  ```python
  num_char = len("Hello")
  print(num_char)  # Outputs: 5
  ```

### Creating User-Defined Functions
- Syntax:
  ```python
  def function_name():
      # indented code block
  ```
- **Steps to Create a Function**:
  1. Use the `def` keyword.
  2. Follow with the function name.
  3. Add parentheses `()` (with parameters inside if needed).
  4. End the line with a colon `:`.
  5. Indent the block of code that belongs to the function.

- Example:
  ```python
  def my_function():
      print("Hello")
      print("Bye")
  ```

### Executing (Calling) Functions
- Functions are executed (called) by writing the function's name followed by parentheses.
  - Example:
    ```python
    my_function()  # Calls the function and prints "Hello" and "Bye"
    ```

### Example: Reeborg's World (Robot Programming)
- [Reeborg's World](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json)
- A tool to practice Python with a virtual robot. 
- Commands like `move()`, `turn_left()` control the robot.

### Creating Custom Commands with Functions
- We can define new functions to combine multiple steps.
- Example: Defining a `turn_around` function
  ```python
  def turn_around():
      turn_left()
      turn_left()
  ```
- Using the function:
  ```python
  move()
  move()
  turn_around()
  move()
  move()
  turn_around()
  ```

### Function Example: Creating `turn_right`
- Since `turn_right` is not a built-in function, we can define it:
  ```python
  def turn_right():
      turn_left()
      turn_left()
      turn_left()
  ```

### Exercise: Drawing a Square with the Robot
- Challenge: Make the robot draw a square.
- Steps:
  ```python
  turn_left()
  move()
  turn_right()
  move()
  turn_right()
  move()
  turn_right()
  move()
  ```

### Benefits of Using Functions
- **Reduces Code Repetition**: Bundle repetitive instructions.
- **Increases Readability**: Easier to understand the code logic.
- **Facilitates Debugging**: Isolate and test specific blocks of functionality.

### Summary
- Functions in Python allow for modular, reusable, and readable code.
- Built-in functions provide essential functionality.
- User-defined functions enable custom behavior.
- Practicing with tools like Reeborg's World reinforces understanding of functions.

## Practice 1 - Reeborg Hurdle Jumping Challenge

[Challenge Link](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json)

**Objective:** Create a program that guides a robot to jump over a series of hurdles and reach the goal using functions, loops, and your knowledge of Python.

**Description:**
You need to program a robot to navigate a path filled with hurdles. The robot must jump over each hurdle to reach the final goal. Your task is to minimize the number of lines of code while keeping your code readable and efficient.

**Instructions:**

1. **Movement Commands:**
   - `move()`: Moves the robot forward by one space.
   - `turn_left()`: Turns the robot to the left.

2. **Function Definitions:**
   - Define a function `turn_right()` to turn the robot to the right by utilizing the `turn_left()` function.
   - Define a function `jump()` that makes the robot jump over a hurdle.

3. **Logic:**
   - Use the defined functions to navigate the robot through the hurdles.
   - Implement a loop to repeat the jumping action for the number of hurdles present.

## Lesson 18 - Indentation

### Importance of Indentation in Python
- Indentation in Python is crucial as it defines the scope and structure of code blocks, such as functions, loops, and conditionals.
- Every line within a function or a block must be indented consistently to signify that it belongs to that block.

### Indentation Basics
- A standard indentation in Python is four spaces.
- Example of a function with proper indentation:
  ```python
  def my_function():
      print("Hello")
      print("World")
  ```
- If a line is not indented, it is considered outside of the block.
  ```python
  def my_function():
      print("Hello")
  print("World")  # This line is outside the function
  ```

### Visualizing Indentation
- Think of a function as a folder containing files. Everything inside the folder is indented to show it belongs to that folder.
- Example:
  - Function (folder)
    - `print("Hello")` (file inside folder)
    - `print("World")` (file inside folder)
  - Code outside function is at the same indentation level as the function definition.

### Indentation with Other Structures
- **If/elif/else Statements:**
  ```python
  def check_sky():
      if sky == "clear":
          print("Blue")
      elif sky == "cloudy":
          print("Grey")
      else:
          print("Unknown")
  ```
- **For Loops:**
  ```python
  for i in range(5):
      print(i)
  ```

### Nested Blocks
- Nested blocks require further indentation for each new level.
  ```python
  def weather_report():
      if sky == "clear":
          if temperature > 20:
              print("Sunny and Warm")
          else:
              print("Sunny but Cool")
      else:
          print("Not Clear")
  ```

### Spaces vs. Tabs Debate
- **Spaces**: Preferred by the Python community and official guidelines.
- **Tabs**: Some developers prefer tabs for reasons such as smaller file sizes and personal preference.
- Official Python style guide (PEP 8) recommends using spaces:
  - Four spaces per indentation level.
  - Mixing tabs and spaces in the same file is not allowed in Python 3.

### Using Code Editors for Indentation
- Most code editors can be configured to handle indentation automatically:
  - Set the editor to use spaces.
  - Configure the tab key to insert four spaces.
  - This ensures consistency and adheres to Python style guidelines.

### Example of Configuring a Code Editor
- Configure your code editor (like VSCode, PyCharm) to convert tabs to spaces:
  - Set the indent size to 4.
  - Enable the option to insert spaces when the tab key is pressed.

### Summary
- Consistent indentation is vital for Python code to function correctly.
- Use four spaces per indentation level.
- Configure your code editor to handle indentation automatically for efficiency.
- Refer to the [Python style guide](https://www.python.org/dev/peps/pep-0008/) for more details on indentation and other style practices.

## Lesson 19 - While Loops

### Introduction to While Loops
- **Definition**: A while loop continues executing as long as a specified condition is true.
- **Comparison to For Loops**:
  - **For Loops**: Used to iterate over a sequence of items (like a list) or a range of numbers.
  - **While Loops**: Used to repeat a block of code as long as a condition is true.

### Syntax of While Loops
- Basic structure:
  ```python
  while condition:
      # code block to be executed repeatedly
  ```

### Example: Simple Robot with While Loop
- A while loop can be used to control a robot's movement:
  ```python
  while is_plugged_in():
      move_forward()
  ```
  - The robot continues moving forward as long as it is plugged in.

### Using While Loops in Practice
- Example from Hurdle 1 challenge:
  ```python
  number_of_hurdles = 6
  while number_of_hurdles > 0:
      jump()
      number_of_hurdles -= 1
      print(number_of_hurdles)
  ```
  - This loop continues until the `number_of_hurdles` is reduced to zero.

### Explanation of Code Execution
- **Initial Condition**: `number_of_hurdles = 6`
- **Loop Execution**:
  - Check if `number_of_hurdles > 0`
  - Execute `jump()`
  - Decrement `number_of_hurdles` by 1
  - Print the current value of `number_of_hurdles`
  - Repeat until `number_of_hurdles` is 0

### Handling Dynamic Conditions
- Example from Hurdle 2 challenge:
  - The goal position is random, so the robot must detect if it has reached the goal.
  ```python
  while (not at_goal()):
      jump()
  ```
  - The loop continues until the robot reaches the goal.

### Important Concepts
- **Condition Checking**: The loop's condition is checked before each iteration.
- **Negation**: `while not at_goal()` is equivalent to `while at_goal() is not True`.

### Choosing Between For and While Loops
- **For Loops**:
  - Ideal for iterating over sequences or ranges.
  - Use when the number of iterations is known.
- **While Loops**:
  - Suitable when the number of iterations is not predetermined.
  - Use when a condition needs to be met to stop the loop.

### Dangers of While Loops: Infinite Loops
- **Infinite Loop**: A loop that never ends because the condition never becomes false.
  ```python
  while 5 > 3:
      jump()
  ```
  - This condition is always true, resulting in an infinite loop.
- **Avoiding Infinite Loops**:
  - Ensure that the condition will eventually become false.
  - Use print statements to debug and understand loop behavior.

### Example: Debugging Infinite Loops
- Print the condition within the loop to monitor its state:
  ```python
  while condition:
      print(condition)
      # code block
  ```

### Conclusion
- **While Loops**: Powerful for repeating tasks until a condition changes.
- **Key Practices**: Ensure conditions are well-defined to avoid infinite loops.

## Practice 2 - Reeborg's Hurdles 3 Challenge using While Loops

[Challenge](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json)

Reeborg has entered a hurdle race. Make him run the course, following the path shown.

*The position and number of hurdles changes each time this world is reloaded.*

**What you need to know**
- The functions `move()` and `turn_left()`.
- The conditions `front_is_clear()` or `wall_in_front()`, `at_goal()`, and their negation.
- How to use a `while` loop and an `if` statement.

Your program should also be valid for worlds Hurdles 1 and Hurdles 2.

## Practice 3 - Reeborg's Hurdles 4 Challenge with variable heights

[Challenge](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json)

Reeborg has entered a hurdle race. Make him run the course, following the path shown.

*The position, the height and the number of hurdles changes each time this world is reloaded.*

**What you need to know**
You should be able to write programs that are valid for worlds Around 4 and Hurdles 3, and ot combine them for this last hurdles race.

Your program should also be valid for worlds Hurdles 1, Hurdles 2 et Hurdles 3

## Project 6  - Reebog's Escaping the Maze

[Challenge](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json)

Reeborg was exploring a dark maze and the battery in its flashlight ran out.

Write a program using an `if/elif/else` statement so Reeborg can find the exit. The secret is to have Reeborg follow along the right edge of the maze, turning right if it can, going straight ahead if it can’t turn right, or turning left as a last resort.

**What you need to know**

- The functions `move()` and `turn_left()`.
- Either the test `front_is_clear()` or `wall_in_front()`, `right_is_clear()` or `wall_on_right()`, and `at_goal()`.
- How to use a `while` loop and `if/elif/else` statements.
- It might be useful to know how to use the negation of a test (`not` in Python).