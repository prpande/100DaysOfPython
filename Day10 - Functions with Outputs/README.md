# Day 10 - Functions with Outputs <!-- omit in toc -->

- [Lesson 22 - Functions with Outputs](#lesson-22---functions-with-outputs)
  - [Overview](#overview)
  - [Types of Functions](#types-of-functions)
  - [Practical Example: Formatting Names](#practical-example-formatting-names)
  - [Explanation of Return Keyword](#explanation-of-return-keyword)
  - [Debugging with Thonny](#debugging-with-thonny)
  - [Built-in Functions](#built-in-functions)
  - [Summary](#summary)
- [Lesson 23 - Multiple return values](#lesson-23---multiple-return-values)
  - [Overview](#overview-1)
  - [Key Concepts](#key-concepts)
  - [Practical Example: Handling Invalid Inputs](#practical-example-handling-invalid-inputs)
  - [Key Takeaways](#key-takeaways)
- [Practice 1 - Days in Month](#practice-1---days-in-month)
- [Lesson 24 - Docstrings](#lesson-24---docstrings)
  - [Overview](#overview-2)
  - [Key Concepts](#key-concepts-1)
  - [Practical Example: Adding Docstrings to Functions](#practical-example-adding-docstrings-to-functions)
  - [Exercise](#exercise)
  - [Key Takeaways](#key-takeaways-1)
- [Project 10 - Calculator](#project-10---calculator)
  - [Overview](#overview-3)
  - [Steps and Key Concepts](#steps-and-key-concepts)
  - [Summary](#summary-1)


## Lesson 22 - Functions with Outputs

### Overview
This lesson focuses on different types of functions in Python, highlighting their purposes and capabilities, including simple functions, functions with inputs, and functions with outputs.

### Types of Functions

1. **Basic Functions**
    - **Definition**: Defined using the `def` keyword, followed by the function name, parentheses `()`, and a colon `:`.
    - **Purpose**: Encapsulates code to be reused multiple times.
    - **Example**:
      ```python
      def greet():
          print("Hello, World!")
      ```

2. **Functions with Inputs**
    - **Definition**: Functions that take parameters within the parentheses.
    - **Purpose**: Allows the function to perform operations using different inputs.
    - **Example**:
      ```python
      def greet(name):
          print(f"Hello, {name}!")
      greet("Alice")  # Outputs: Hello, Alice!
      ```

3. **Functions with Outputs**
    - **Definition**: Functions that return a value using the `return` keyword.
    - **Purpose**: Provides a result from the function which can be used later in the code.
    - **Example**:
      ```python
      def add(a, b):
          return a + b
      result = add(3, 4)  # result is 7
      ```

### Practical Example: Formatting Names
1. **Function Definition**
    - Purpose: Convert first and last names to title case.
    - Steps:
      1. Define the function with two parameters: `f_name` and `l_name`.
      2. Convert each name to title case using the `title()` method. [more info](https://stackoverflow.com/questions/8347048/how-to-convert-string-to-title-case-in-python)
      3. Return the formatted full name.

2. **Code Implementation**
    ```python
    def format_name(f_name, l_name):
        formatted_f_name = f_name.title()
        formatted_l_name = l_name.title()
        return f"{formatted_f_name} {formatted_l_name}"
    
    formatted_name = format_name("angela", "YU")
    print(formatted_name)  # Outputs: Angela Yu
    ```

### Explanation of Return Keyword
- **Purpose**: To output a value from the function which can replace the function call in the code.
- **Example**:
  ```python
  def square(number):
      return number * number
  result = square(5)  # result is 25
  ```

### Debugging with Thonny
- **Visualization**: Step through the function call to see how inputs are processed and outputs are returned.
- **Example**:
  - Function call with parameters.
  - Execution within the function.
  - Return value replacing the function call.

### Built-in Functions
- Example: `len()` function
  - Takes an input (e.g., a string) and returns an output (length of the string).
  - Code:
    ```python
    length = len("Angela")
    print(length)  # Outputs: 6
    ```

### Summary
- Functions are essential for creating reusable code.
- Functions can take inputs (parameters) to perform dynamic operations.
- Functions can return outputs using the `return` keyword, enabling the function to provide results back to the calling code.
- Understanding and utilizing these types of functions enhances code efficiency and readability.

## Lesson 23 - Multiple return values

### Overview
In this lesson, we explored the use of multiple return statements within a single function. We examined how return statements influence the flow of the function and how they can be utilized for early exits and error handling.

### Key Concepts

1. **Function Termination with Return**
    - When the computer encounters a `return` statement, it terminates the function immediately.
    - Any code written after a `return` statement within the same function will not be executed.

2. **Multiple Return Statements**
    - Functions can contain multiple `return` statements.
    - Useful for terminating a function early under certain conditions, known as early returns.

3. **Empty Return Statement**
    - Using `return` without any value terminates the function and returns `None`.

### Practical Example: Handling Invalid Inputs

1. **Original Function: `format_name`**
    - Converts first and last names to title case and returns the formatted string.
    - Example:
      ```python
      def format_name(f_name, l_name):
          formatted_f_name = f_name.title()
          formatted_l_name = l_name.title()
          return f"{formatted_f_name} {formatted_l_name}"
      ```

2. **Enhancing the Function with Early Returns**
    - Add checks for empty input strings and handle them appropriately.
    - Example with early return and meaningful messages:
      ```python
      def format_name(f_name, l_name):
          if f_name == "" or l_name == "":
              return "Invalid input: First name and last name cannot be empty."
          
          formatted_f_name = f_name.title()
          formatted_l_name = l_name.title()
          return f"{formatted_f_name} {formatted_l_name}"
      ```

3. **Interactive Input Example**
    - Using `input()` to get user inputs and handling cases where inputs might be empty.
    - Example:
      ```python
      def format_name(f_name, l_name):
          if f_name == "" or l_name == "":
              return "Invalid input: First name and last name cannot be empty."
          
          formatted_f_name = f_name.title()
          formatted_l_name = l_name.title()
          return f"{formatted_f_name} {formatted_l_name}"
      
      first_name = input("What is your first name? ")
      last_name = input("What is your last name? ")
      
      formatted_name = format_name(first_name, last_name)
      print(formatted_name)
      ```

### Key Takeaways

1. **Early Return for Error Handling**
    - Early returns can prevent unnecessary processing when certain conditions are met, improving the efficiency and readability of the function.
    - Example of an early return:
      ```python
      def format_name(f_name, l_name):
          if f_name == "" or l_name == "":
              return "Invalid input: First name and last name cannot be empty."
          # Additional processing
      ```

2. **Multiple Return Statements**
    - Using multiple return statements can make the function logic clearer and handle different scenarios appropriately.
    - Example:
      ```python
      def check_value(val):
          if val < 0:
              return "Negative value"
          elif val == 0:
              return "Zero value"
          else:
              return "Positive value"
      ```

3. **Importance of Meaningful Return Messages**
    - Returning meaningful messages helps in debugging and informs the user or developer about the state of the function.

## Practice 1 - Days in Month

***Convert the `is_leap()` function***

In the starting code, you'll find the solution from the Leap Year challenge. First, convert this function `is_leap()` so that instead of printing "Leap year." or "Not leap year." it should **return** `True` if it is a leap year and **return** `False` if it is not a leap year.

***Create a new function called `days_in_month()`***

You are then going to modify a function called `days_in_month()` which will take a **year** and a **month** as inputs, e.g.

```
days_in_month(year=2022, month=2)
```

And it will use this information to work out if the year is a leap year and decide the **number of days in the month**, then **return** that as the **output, e.g.:**

```
28
```

The List month_days contains the number of days in a month from January to December for a non-leap year. A leap year has 29 days in February.

**Hint**

- Look at the function call at the bottom of the code to see the positional arguments. The order is very important.
- Feel free to choose your own parameter names.
- Remember that `month_days` is a List and Lists in Python start at position 0. So the number of days in January is `month_days[0]`
- Be careful with indentation.

## Lesson 24 - Docstrings

### Overview
In this lesson, we discussed the concept of docstrings in Python, which are used to create documentation for functions and other blocks of code. Docstrings help in understanding what a function does, especially when revisiting the code in the future or when others use your functions.

### Key Concepts

1. **Definition of Docstrings**
    - Docstrings are string literals that appear right after the definition of a function, method, class, or module.
    - They are used to describe what the function or block of code does.

2. **Syntax of Docstrings**
    - A docstring is written as the first indented line after the function declaration.
    - Enclosed within triple quotes (`"""`), allowing the string to span multiple lines.
    - Example:
      ```python
      def format_name(f_name, l_name):
          """
          Takes a first and last name and formats it to return the title case version of the name.
          """
          formatted_f_name = f_name.title()
          formatted_l_name = l_name.title()
          return f"{formatted_f_name} {formatted_l_name}"
      ```

3. **Multi-line Strings in Docstrings**
    - Docstrings can span multiple lines, making it easier to provide detailed descriptions.
    - Example:
      ```python
      """
      This function takes a first name and a last name,
      converts them to title case, and returns the formatted full name.
      """
      ```

4. **Viewing Docstrings**
    - When calling the function in an interactive environment (e.g., Jupyter Notebook, Python shell), opening the parentheses after the function name will show the docstring as a tooltip or help text.
    - Example:
      ```python
      format_name(
      ```
      This would show: "Takes a first and last name and formats it to return the title case version of the name."

5. **Using Docstrings as Comments**
    - Docstrings can serve as multi-line comments, but this is not their primary purpose.
    - For multi-line comments, it's better to use `#` for each line or use the keyboard shortcut (Command + / or Control + /) to comment out multiple lines of code.

6. **Official Python Guidance**
    - The official Python style guide (PEP 8) recommends using docstrings for documentation.
    - Multi-line comments using `#` are preferred over using triple quotes for comments not assigned to variables.

### Practical Example: Adding Docstrings to Functions

1. **Original Function: `format_name`**
    - Adding a docstring:
      ```python
      def format_name(f_name, l_name):
          """
          Takes a first and last name and formats it to return the title case version of the name.
          """
          formatted_f_name = f_name.title()
          formatted_l_name = l_name.title()
          return f"{formatted_f_name} {formatted_l_name}"
      ```

2. **Calling the Function with Docstring**
    - Example call to view the docstring:
      ```python
      format_name(
      ```

### Exercise
- Add docstrings to the functions you have previously created.
- Verify that the docstrings appear when you call the functions in an interactive Python environment.

### Key Takeaways
- Docstrings provide a way to document functions directly within the code.
- Use triple quotes for docstrings to allow multi-line descriptions.
- Docstrings help users understand the purpose and usage of functions.
- Follow PEP 8 guidelines for writing clear and concise docstrings.

## Project 10 - Calculator

[Demo](https://appbrewery.github.io/python-day10-demo/)

### Overview
In this project, we aim to build a basic calculator program that can perform addition, subtraction, multiplication, and division. The calculator will take two numbers from the user, perform the selected operation, and display the result. The user can continue calculations with the result or start a new calculation.

### Steps and Key Concepts

1. **Define Mathematical Functions**
    - Create functions for addition, subtraction, multiplication, and division.
    - Each function will take two arguments and return the result of the respective operation.

2. **Store Functions in a Dictionary**
    - Use a dictionary to map operation symbols to the corresponding functions.
    - This allows dynamic selection of the function based on user input.

3. **User Input for Calculation**
    - Prompt the user for the first number, the operation, and the second number.
    - Convert input strings to integers for numerical operations.

4. **Perform the Calculation**
    - Retrieve the selected function from the dictionary using the operation symbol.
    - Call the function with the user-provided numbers and print the result.

5. **Continuous Calculation**
    - Allow the user to continue calculations with the result or start a new calculation.
    - Implement a loop to handle repeated calculations or exit based on user input.

### Summary
- **Functions:** Defined for each arithmetic operation.
- **Dictionary:** Maps symbols to corresponding functions.
- **User Input:** Prompts for numbers and operation, converts input to appropriate type.
- **Loop:** Allows continuous calculation with result or restarts calculation.

