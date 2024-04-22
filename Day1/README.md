# Day 1 <!-- omit in toc -->


- [Lesson 1 - PRINTING](#lesson-1---printing)
    - [Writing and Running Code](#writing-and-running-code)
    - [Troubleshooting and Error Handling](#troubleshooting-and-error-handling)
  - [Practice](#practice)
    - [Example Output](#example-output)
  - [Print Modifiers](#print-modifiers)
- [Lesson 2 - DEBUGGING PRACTICE \& String Manipulation](#lesson-2---debugging-practice--string-manipulation)
    - [Advanced String Operations](#advanced-string-operations)
    - [Understanding and Handling Errors](#understanding-and-handling-errors)
    - [Debugging Tips](#debugging-tips)
  - [Practice](#practice-1)
    - [Example Output](#example-output-1)
- [Lesson 3 - Introduction to the `input()` Function and Nested Functions in Python](#lesson-3---introduction-to-the-input-function-and-nested-functions-in-python)
    - [Using the `input()` Function](#using-the-input-function)
    - [Nested Functions](#nested-functions)
    - [Debugging with Thonny](#debugging-with-thonny)
    - [Effective Code Documentation](#effective-code-documentation)
    - [Keyboard Shortcuts for Efficiency](#keyboard-shortcuts-for-efficiency)
  - [Practice](#practice-2)
      - [Example Input](#example-input)
      - [Example Output](#example-output-2)
- [Lesson 4 - VARIABLES](#lesson-4---variables)
  - [Basic Concept of Variables](#basic-concept-of-variables)
  - [Using Variables](#using-variables)
  - [Practical Example](#practical-example)
  - [Manipulating Variables](#manipulating-variables)
  - [Using Variables to Simplify Code](#using-variables-to-simplify-code)
  - [Importance of Variable Names](#importance-of-variable-names)
  - [Mutability of Variables](#mutability-of-variables)
  - [Practice](#practice-3)
    - [Example Input 1](#example-input-1)
    - [Example Output 1](#example-output-1)
    - [Example Input 2](#example-input-2)
    - [Example Output 2](#example-output-2)
  - [Best Practices for Naming Variables](#best-practices-for-naming-variables)
    - [Principles of Variable Naming](#principles-of-variable-naming)
    - [Syntax Rules for Variable Names](#syntax-rules-for-variable-names)
    - [Practical Tips for Variable Names](#practical-tips-for-variable-names)
    - [Example of Variable Naming and Usage](#example-of-variable-naming-and-usage)
- [Day 1 Project: Band Name Generator](#day-1-project-band-name-generator)
    - [Project Overview](#project-overview)
    - [Enhancing User Experience](#enhancing-user-experience)


## Lesson 1 - PRINTING

#### Writing and Running Code

1. **Creating a Print Function:**
   - The `print()` function is used to output text or variables to the console.
   - Example:
     ```python
     print("Hello world!")
     ```

2. **Understanding Strings:**
   - Strings are sequences of characters enclosed in quotes. Ensure you close your strings properly to avoid syntax errors.
   - Example:
     ```python
     print("Hello, world!")
     ```

3. **Common Syntax Errors:**
   - Missing a closing quote will change the syntax highlighting and cause an error.
   - Syntax errors are indicated in the console in red text. The error message will help identify what needs to be corrected.

#### Troubleshooting and Error Handling

1. **Identifying Errors:**
   - Pay attention to syntax highlighting as it can provide hints about potential errors.
   - Missing punctuation like a closing quote or parenthesis can lead to errors that prevent your code from executing.

2. **Using External Resources:**
   - If encountering an unfamiliar error, search the error message on Google or Stack Overflow. Often, other developers have encountered similar issues and have shared their solutions.

3. **Practical Example of Error Resolution:**
   - If you encounter a syntax error indicating a missing double quote, add the quote and rerun the code. Observe the change in syntax highlighting and output to ensure the issue is resolved.

### Practice

Write a program that uses print statements to print the following recipe into the Output console. The text to print is already there, you just need to make it into code. Your code should print all five lines exactly the same as the example output below.

#### Example Output
```
1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.
2. Knead the dough for 10 minutes.
3. Add 3g of Salt.
4. Leave to rise for 2 hours.
5. Bake at 200 degrees C for 30 minutes.
```

### Print Modifiers

```python
print("A 'single quote' inside a double quote")
print('A "double quote" inside a single quote')
print("Alternatively you can just \"escape\" the quote")
```

## Lesson 2 - DEBUGGING PRACTICE & String Manipulation

#### Advanced String Operations

1. **Creating New Lines in Strings:**
   - To print multiple lines using a single `print()` function, use the newline character `\n`.
   - Example:
     ```python
     print("Hello\nworld")
     ```
   - This code will print "Hello" on the first line and "world" on the second line.

2. **Concatenating Strings:**
   - Strings can be combined using the `+` operator.
   - Example:
     ```python
     print("Hello" + " " + "world")
     ```
   - If you need a space between words, include a string with a space `" "` between the other strings.

#### Understanding and Handling Errors

1. **Indentation Error:**
   - Python uses indentation to define the structure of the code. Incorrect indentation leads to an `IndentationError`.
   - Example of incorrect indentation:
     ```python
      print("Hello world")  # unexpected indent
     ```
   - Ensure all code starts at the beginning of the line unless it is part of a code block that requires indentation.

2. **Syntax Error:**
   - Errors in the syntax of the language, such as missing quotes or parentheses, will prevent the code from executing.
   - Example:
     ```python
     print("Hello world  # missing closing quote
     ```
   - Pay attention to syntax highlighting in your editor, which can help identify such errors before running the code.

#### Debugging Tips

1. **Utilize Code Intelligence:**
   - Modern IDEs and code editors offer code intelligence features like auto-completion and error highlighting.
   - Enabling these features can help catch errors early by showing warnings or error messages as you type.

2. **Stack Overflow and Google:**
   - Use these resources to search for error messages and find explanations and solutions. Often, the issues you encounter have been faced and solved by other developers.

3. **Practice Debugging:**
   - Engage in exercises designed to improve your debugging skills. Correct pre-written code with bugs to understand common mistakes and learn how to fix them.

### Practice
Look at the code in the code editor on the left. There are errors on all 4 lines of code. Fix the code so that it runs without errors.

```python
# Fix the code below 👇

print(Day 1 - String Manipulation")
print("String Concatenation is done with the "+" sign.")
  print('e.g. print("Hello " + "world")')
print(("New lines can be created with a backslash and n.")
```

#### Example Output
```
Day 1 - String Manipulation
String Concatenation is done with the "+" sign.
e.g. print( "Hello " + "world" )
New lines can be created with a backslash and n.
```

## Lesson 3 - Introduction to the `input()` Function and Nested Functions in Python

`input()` function in Python, which allows for interactive user input. This function is crucial for creating dynamic programs that can receive data from users and utilize it within the program.

#### Using the `input()` Function

1. **Basic Usage**:
   - The `input()` function pauses program execution to allow the user to type something into the console. Once the user presses Enter, the program resumes.
   - Example:
     ```python
     input("What is your name? ")
     ```

2. **Understanding the Function**:
   - When `input()` is called, it displays a prompt to the user and waits for input.
   - The function returns the string that was entered by the user.

#### Nested Functions

1. **Combining `input()` and `print()`**:
   - You can nest the `input()` function within a `print()` function to handle user input and output in a single line of code.
   - Example:
     ```python
     print("Hello, " + input("What is your name? "))
     ```

2. **Execution Flow**:
   - The `input()` function inside the `print()` statement first executes to collect user input.
   - The return value from `input()` is then immediately used as part of the `print()` statement.

#### Debugging with Thonny

1. **Using Thonny for Step-by-Step Execution**:
   - https://thonny.org/
   - Thonny is a Python IDE that allows for step-by-step execution of code, which can be extremely helpful for beginners to understand how Python processes each part of the code.
   - It can demonstrate how expressions are evaluated and how data flows through functions.

2. **Practical Application**:
   - Install Thonny from thonny.org and use it to step through complex pieces of code to better understand how Python executes each statement and handles functions like `input()` and `print()`.

#### Effective Code Documentation

1. **Commenting Code**:
   - Comments are made in Python using the `#` symbol.
   - These are crucial for documenting what certain parts of the code do, especially for complex operations or where the purpose of the code might not be immediately clear.

2. **Using Comments to Enhance Understanding**:
   - Add comments above tricky sections of code or new concepts to explain their functionality in your own words.
   - This practice helps when revisiting code after some time, as the comments act as reminders of what each section of code is intended to do.

#### Keyboard Shortcuts for Efficiency

- **Commenting Out Code**:
  - Quickly comment or uncomment lines of code using keyboard shortcuts:
    - Mac: `Command` + `/`
    - Windows/Linux: `Control` + `/`

- **Undo Changes**:
  - Undo recent changes with:
    - Mac: `Command` + `Z`
    - Windows/Linux: `Control` + `Z`

### Practice

Write a program that calculates and outputs the number of characters in any name. The automated tests will try out lots of different names as the input. Your code should work for any name. Your code should only output the number, no other text is needed.

> You can use `len()` around any piece of text to calculate the number of characters.  
> e.g. https://www.google.com/search?q=how+to+get+the+length+of+a+string+in+python+stack+overflow

##### Example Input

```
John
```

John = 4 characters

##### Example Output

```
4
```

## Lesson 4 - VARIABLES

### Basic Concept of Variables
- Variables are used to store data values.
- A variable in Python is created by assigning a value to a variable name.
- Example:
  ```python
  name = input("Please enter your name: ")
  ```

### Using Variables
- Once a variable is defined, it can be used anywhere in the program.
- Variables can hold different types of data like numbers, strings, lists, etc.
- The value of a variable can be changed or updated throughout the program.

### Practical Example
- Start by collecting user input and assigning it to a variable:
  ```python
  name = input("Please enter your name: ")
  ```
- Print the value stored in the variable:
  ```python
  print(name)
  ```
- The variable `name` holds the input value, making it accessible anywhere in the code after its declaration.

### Manipulating Variables
- Variables can be reassigned to hold different data.
- Example of changing variable value:
  ```python
  name = "Jack"
  print(name)  # Output: Jack
  name = "Angela"
  print(name)  # Output: Angela
  ```

### Using Variables to Simplify Code
- Variables can break down operations into simpler steps.
- Example with the `len()` function:
  ```python
  name = input("Enter your name: ")
  length_of_name = len(name)
  print(length_of_name)
  ```
- This approach makes the code cleaner and more readable by using variables to store intermediate results.

### Importance of Variable Names
- Variable names should be descriptive to make the code more understandable.
- Just as names in a phonebook help identify a number, variable names help identify stored data.

### Mutability of Variables
- As implied by the term "variable", the data stored can change (or vary) over time.
- Variables provide flexibility to modify the data they hold, which is useful for handling dynamic data in programs.

### Practice

This program takes two inputs. The first input is stored in a variable called a. The second input is stored in a variable called b.

Write a program that switches the values stored in the variables a and b.

```python
# There are two variables, a and b from input
a = input()
b = input()
# 🚨 Don't change the code above ☝️
####################################
# Write your code below this line 👇




# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)
```

Warning . You don't need to print anything. The print statement is already in the template code. However, your program should work for different inputs. e.g. any value of a and b.

#### Example Input 1

```
29
41
```

#### Example Output 1

```
a: 41
b: 29
```

#### Example Input 2

```
Hello
World
```

#### Example Output 2

```
a: World
b: Hello
```

### Best Practices for Naming Variables

#### Principles of Variable Naming
- **Clarity and Readability:** Variable names should be self-explanatory. Names like `n` or `l` might not be clear after some time, making it difficult to understand the code later. Choose meaningful names that reflect the data they hold, e.g., `username` instead of just `n`.
  
- **Descriptive Names:** Instead of single letters, use descriptive names that convey the purpose or nature of the data, such as `username` for a user's name or `total_amount` for representing an amount.

#### Syntax Rules for Variable Names
- **No Spaces:** Variable names cannot contain spaces. Use underscores to separate words in variable names, e.g., `user_name` instead of `user name`.
  
- **Use of Numbers:** Numbers can be included in variable names but not at the beginning. For example, `length1` is valid, but `1length` is invalid and will result in a syntax error.
  
- **Avoid Reserved Words:** Avoid using Python’s reserved words (like `print`, `input`, etc.) as variable names. These are part of Python's syntax for built-in functions, and using them as variable names can lead to confusing code and errors.

#### Practical Tips for Variable Names
- **Consistency:** If you decide on a particular name, stay consistent with its spelling. Inconsistent naming or typos can lead to runtime errors, e.g., a `NameError` if you accidentally mistype a variable name like typing `nama` instead of `name`.

- **Case Sensitivity:** Remember that Python is case-sensitive. For instance, `Name` and `name` would be treated as two distinct variables.

- **Avoiding Errors:** Misnaming a variable leads to `NameError` indicating that a variable is not defined. This typically occurs when there is a mismatch between the declared variable name and the one being referenced in your code.

#### Example of Variable Naming and Usage
```python
# Good practice
user_name = input("Please enter your username: ")
length_of_username = len(user_name)
print(length_of_username)

# Bad practice
n = input("Please enter your username: ")
l = len(n)
print(l)
```

## Day 1 Project: Band Name Generator

#### Project Overview
In this project, you will build a band name generator using Python. This program will prompt the user for the name of the city they grew up in and the name of their pet, then it will combine these answers to generate a potential band name.

```python
#1. Create a greeting for your program.

#2. Ask the user for the city that they grew up in.

#3. Ask the user for the name of a pet.

#4. Combine the name of their city and pet and show them their band name.

#5. Make sure the input cursor shows on a new line.
```

#### Enhancing User Experience

- **Ensure Inputs Appear on New Lines**:
  - To make the inputs appear on new lines (enhancing readability), add a newline character (`\n`) at the end of your input prompt strings.
