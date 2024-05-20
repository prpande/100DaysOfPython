# Day 8 - Function Parameters & Caesar Cipher<!-- omit in toc -->

- [Lesson 20 - Functions with Inputs](#lesson-20---functions-with-inputs)
  - [Overview](#overview)
  - [Defining and Calling Functions](#defining-and-calling-functions)
  - [Creating and Using a Basic Function](#creating-and-using-a-basic-function)
  - [Enhancing Functions with Inputs](#enhancing-functions-with-inputs)
  - [Parameters vs. Arguments](#parameters-vs-arguments)
  - [Example to Illustrate Parameters and Arguments](#example-to-illustrate-parameters-and-arguments)
  - [Practical Usage of Parameters](#practical-usage-of-parameters)
  - [Summary](#summary)
  - [Key Terms](#key-terms)
- [Lesson 21 - Positional vs. Keyword Arguments](#lesson-21---positional-vs-keyword-arguments)
  - [Overview](#overview-1)
  - [Functions with Multiple Inputs](#functions-with-multiple-inputs)
  - [Positional Arguments](#positional-arguments)
  - [Keyword Arguments](#keyword-arguments)
  - [Example with Multiple Parameters](#example-with-multiple-parameters)
  - [Positional vs. Keyword Arguments](#positional-vs-keyword-arguments)
  - [Challenge Exercise](#challenge-exercise)
  - [Summary](#summary-1)
  - [Key Terms](#key-terms-1)
- [Practice 1 - Paint Area Calculator](#practice-1---paint-area-calculator)
- [Practice 2 -  Prime Numbers](#practice-2----prime-numbers)
- [Project 8 - Caesar Cipher](#project-8---caesar-cipher)
  - [Objective](#objective)
  - [Background](#background)
  - [Requirements](#requirements)
  - [Example Workflow](#example-workflow)
  - [Part 1 - Encryption](#part-1---encryption)
    - [Encoding Process](#encoding-process)
    - [Project Overview](#project-overview)
    - [Step-by-Step Implementation](#step-by-step-implementation)
    - [Practical Example and Testing](#practical-example-and-testing)
    - [Code Walkthrough and Debugging](#code-walkthrough-and-debugging)
  - [Part 2 - Decryption](#part-2---decryption)
    - [Objective](#objective-1)
    - [Key Concepts](#key-concepts)
    - [Implementation Steps](#implementation-steps)
    - [Testing the Function](#testing-the-function)
    - [Debugging and Edge Cases](#debugging-and-edge-cases)
  - [Part 3 - Reorganizing our code](#part-3---reorganizing-our-code)
    - [Objective](#objective-2)
    - [Key Concepts](#key-concepts-1)
    - [Implementation Steps](#implementation-steps-1)
    - [Testing and Debugging](#testing-and-debugging)
    - [Conclusion](#conclusion)
  - [Part 4 - UI improvements](#part-4---ui-improvements)
    - [To-Do List](#to-do-list)
  - [Summary](#summary-2)



## Lesson 20 - Functions with Inputs

### Overview
Functions in Python are blocks of reusable code designed to perform a specific task. Functions help in organizing code by breaking complex sets of instructions into manageable pieces. This makes code easier to understand, test, and maintain.

### Defining and Calling Functions
1. **Defining a Function**:
   - Use the `def` keyword followed by the function name and parentheses `()`.
   - Example:
     ```python
     def greet():
         print("Hello")
         print("How do you do?")
         print("Nice weather, isn't it?")
     ```

2. **Calling a Function**:
   - To execute the function, simply type its name followed by parentheses.
   - Example:
     ```python
     greet()
     ```
   - When this line is executed, Python searches for the function definition and runs the code within it.

### Creating and Using a Basic Function
- **Step-by-Step Example**:
  1. Define the function using `def` keyword:
     ```python
     def greet():
         print("Hello")
         print("How do you do?")
         print("Nice weather, isn't it?")
     ```
  2. Call the function:
     ```python
     greet()
     ```
  - This will output:
    ```
    Hello
    How do you do?
    Nice weather, isn't it?
    ```

### Enhancing Functions with Inputs
Functions can be made more versatile by allowing inputs (parameters), enabling different outputs based on the given inputs.

1. **Adding Parameters**:
   - Define a function that takes a parameter.
   - Example:
     ```python
     def greet_with_name(name):
         print(f"Hello, {name}")
         print(f"How do you do, {name}?")
         print("Nice weather, isn't it?")
     ```

2. **Calling the Function with an Argument**:
   - Pass an argument when calling the function.
   - Example:
     ```python
     greet_with_name("Angela")
     ```
   - This will output:
     ```
     Hello, Angela
     How do you do, Angela?
     Nice weather, isn't it?
     ```

### Parameters vs. Arguments
- **Parameter**: The variable listed inside the parentheses in the function definition.
- **Argument**: The actual value passed to the function when it is called.

### Example to Illustrate Parameters and Arguments
1. **Function Definition**:
   ```python
   def greet_with_name(name):
       print(f"Hello, {name}")
       print(f"How do you do, {name}?")
   ```

2. **Function Call with Argument**:
   ```python
   greet_with_name("Jack Bauer")
   ```
   - Here, `name` is the parameter, and `"Jack Bauer"` is the argument.

### Practical Usage of Parameters
- Allows functions to handle different inputs and produce dynamic outputs.
- Promotes code reuse by making functions adaptable to various situations.

### Summary
- **Functions** encapsulate reusable code blocks.
- **Defining a function** involves using the `def` keyword.
- **Calling a function** executes the code within the function.
- **Parameters** and **arguments** allow functions to process different inputs, enhancing their flexibility and usefulness.

### Key Terms
- **Function**: A named section of a code that performs a specific task.
- **Parameter**: A variable in a function definition that receives an argument.
- **Argument**: The actual value supplied to a function when it is called.

## Lesson 21 - Positional vs. Keyword Arguments

### Overview
In this lesson, we expanded our understanding of functions by exploring how to create functions that accept multiple inputs. This enhances the flexibility and usability of functions, allowing them to handle various inputs and produce dynamic outputs.

### Functions with Multiple Inputs
1. **Defining a Function with Multiple Parameters**:
   - Functions can take more than one parameter by separating each parameter with a comma.
   - Example:
     ```python
     def greet_with(name, location):
         print(f"Hello, {name}")
         print(f"What is it like in {location}?")
     ```

2. **Calling a Function with Multiple Arguments**:
   - When calling a function with multiple parameters, provide the arguments in the same order as the parameters.
   - Example:
     ```python
     greet_with("Jack Bauer", "nowhere")
     ```
   - This will output:
     ```
     Hello, Jack Bauer
     What is it like in nowhere?
     ```

### Positional Arguments
- **Definition**: Arguments passed to a function based on their position.
- **Order Matters**: The first argument is assigned to the first parameter, the second argument to the second parameter, and so on.
- **Example**:
  ```python
  greet_with("nowhere", "Jack Bauer")
  ```
  - This will incorrectly output:
    ```
    Hello, nowhere
    What is it like in Jack Bauer?
    ```
  - The order of arguments does not match the intended parameters, causing incorrect output.

### Keyword Arguments
- **Definition**: Arguments passed to a function using the parameter names.
- **Advantages**: Makes the function calls clearer and reduces errors by explicitly associating each argument with a parameter.
- **Syntax**:
  ```python
  greet_with(name="Angela", location="London")
  ```
- **Flexibility**: The order of keyword arguments can be switched without affecting the output.
  - Example:
    ```python
    greet_with(location="London", name="Angela")
    ```
  - This still correctly outputs:
    ```
    Hello, Angela
    What is it like in London?
    ```

### Example with Multiple Parameters
1. **Function Definition**:
   ```python
   def greet_with(name, location):
       print(f"Hello, {name}")
       print(f"What is it like in {location}?")
   ```

2. **Calling with Positional Arguments**:
   ```python
   greet_with("Jack Bauer", "nowhere")
   ```
   - Outputs:
     ```
     Hello, Jack Bauer
     What is it like in nowhere?
     ```

3. **Calling with Keyword Arguments**:
   ```python
   greet_with(name="Angela", location="London")
   ```
   - Outputs:
     ```
     Hello, Angela
     What is it like in London?
     ```

### Positional vs. Keyword Arguments
- **Positional Arguments**:
  - Relies on the order of arguments.
  - Example:
    ```python
    def func(a, b, c):
        print(a, b, c)

    func(1, 2, 3)
    ```
  - a=1, b=2, c=3.
- **Keyword Arguments**:
  - Uses explicit parameter names.
  - Example:
    ```python
    func(a=1, b=2, c=3)
    ```

### Challenge Exercise
1. **Task**: Convert the function call `greet_with(name, location)` to use keyword arguments.
2. **Solution**:
   ```python
   greet_with(name="Angela", location="London")
   ```

### Summary
- Functions can accept multiple inputs by adding multiple parameters.
- Positional arguments depend on the order of the arguments.
- Keyword arguments explicitly define which parameter each argument is for, providing more clarity and reducing errors.
- Use keyword arguments to make your code more readable and less prone to mistakes, especially when dealing with functions that take multiple parameters.

### Key Terms
- **Parameter**: A variable in a function definition that receives an argument.
- **Argument**: The actual value supplied to a function when it is called.
- **Positional Argument**: An argument that is assigned to a parameter based on its position in the function call.
- **Keyword Argument**: An argument that is assigned to a parameter based on the parameter name.

## Practice 1 - Paint Area Calculator

You are painting a wall. The instructions on the paint can says that **1 can of paint can cover 5 square meters** of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

```
number of cans = (wall height x wall width) ÷ coverage per can
```

e.g. Height = 2, Width = 4, Coverage = 5

```
number of cans = (2 * 4) / 5
               = 1.6
```

But because you can't buy 0.6 of a can of paint, the result should be **rounded up to 2** cans.

**IMPORTANT**: Notice the name of the function and parameters must match those on line 13 for the code to work.

**Example Input**
```
3
9
```
**Example Output**
```
You'll need 6 cans of paint.
```
**Hint**

[Stackoveflow link](https://stackoverflow.com/questions/2356501/how-do-you-round-up-a-number-in-python) on how to round up a number: 

## Practice 2 -  Prime Numbers

Prime numbers are numbers that can only be cleanly divided by themselves and 1.

https://en.wikipedia.org/wiki/Prime_number

**You need to write a function** that checks whether if the number passed into it is a prime number or not.

e.g. 2 is a prime number because it's only divisible by 1 and 2.

But 4 is not a prime number because you can divide it by 1, 2 or 4.

**Example Input 1**
```
73
```
**Example Output 1**
```
It's a prime number.
```
**Example Input 2**
```
75
```
**Example Output 2**
```
It's not a prime number.
```

## Project 8 - Caesar Cipher

[Demo](https://appbrewery.github.io/python-day8-demo/) 

### Objective

Develop a Caesar Cipher encryption and decryption program in Python that utilizes functions to handle user inputs, encode messages by shifting letters, and decode messages using the specified shift.

### Background

The Caesar Cipher is an ancient encryption technique used by Julius Caesar to securely transmit military messages. Each letter in the plaintext is shifted a certain number of places down the alphabet. For instance, with a shift of 3, A becomes D, B becomes E, and so forth. This project aims to implement a program that can both encode and decode messages using this method.

### Requirements

1. **Understanding Functions with Inputs:**
   - Learn how to create functions that accept inputs (parameters) and utilize them in various operations.
   - Understand the difference between parameters (defined in the function) and arguments (actual values passed to the function).

2. **Program Features:**
   - **Encoding Messages:**
     - Function to encode a message by shifting each letter by a user-defined number.
     - The program should accept a message (without spaces) and a shift number as inputs.
     - Output the encoded message.

   - **Decoding Messages:**
     - Function to decode a message by shifting each letter back by the same user-defined number.
     - The program should accept an encoded message and the shift number as inputs.
     - Output the decoded message.

3. **User Interaction:**
   - Provide a menu or prompt for the user to choose between encoding and decoding.
   - Ensure the program can handle invalid inputs gracefully.
   - Allow the user to perform multiple operations without restarting the program.

### Example Workflow

1. User selects "encode" to start the encryption process.
2. User inputs the message (e.g., "HELLO").
3. User inputs the shift number (e.g., 3).
4. The program outputs the encoded message (e.g., "KHOOR").
5. User selects "decode" to start the decryption process.
6. User inputs the encoded message (e.g., "KHOOR").
7. User inputs the shift number (e.g., 3).
8. The program outputs the original message (e.g., "HELLO").

### Part 1 - Encryption

#### Encoding Process

- **Principle**: Shift each letter in the plaintext by a specified number of positions down the alphabet.
- **Artifacts**: Historically, devices like rotating dials were used to encode messages by aligning letters with their shifted counterparts.

#### Project Overview

- **Goal**: Create a digital version of the Caesar Cipher that can both encode and decode messages.
- **Starting Code**:
  - The alphabet stored in a list.
  - User inputs for the operation (encode or decode), the message, and the shift amount.

#### Step-by-Step Implementation
1. **User Inputs**:
   - Direction (`encode` or `decode`)
   - Message (converted to lowercase)
   - Shift number (converted to an integer)

2. **Creating the Encrypt Function**:
   - **Definition**: Use `def encrypt(plain_text, shift_amount)` to define the function.
   - **Loop through Plain Text**:
     - For each letter, find its position in the alphabet.
     - Calculate the new position by adding the shift amount.
     - Append the new letter to the result string.

3. **Handling Shifts Beyond 'Z'**:
   - Duplicate the alphabet list to handle cases where shifting goes beyond 'Z'.
   - Ensure that the function can handle wrap-around scenarios correctly.

4. **Testing the Encrypt Function**:
   - Example: Encoding "hello" with a shift of 5 should output "mjqqt".
   - Ensure to handle edge cases like shifting letters at the end of the alphabet (e.g., "zulu" with a shift of 5).

#### Practical Example and Testing
- **Initial Test**:
  - Direction: `encode`
  - Message: `hello`
  - Shift: `5`
  - Output: `mjqqt`
- **Edge Case Test**:
  - Message: `zulu`
  - Shift: `5`
  - Output: Handle index error and produce correct output by looping back to start of the alphabet.

#### Code Walkthrough and Debugging
1. **Encrypt Function Implementation**:
   - Define the function with two parameters: `plain_text` and `shift_amount`.
   - Use a for loop to iterate through each letter in the input text.
   - Use `alphabet.index(letter)` to find the current position.
   - Calculate the new position and append the corresponding letter to the ciphertext.
   - Handle wrapping by duplicating the alphabet list.
   - Print the encrypted text.

2. **Debugging**:
   - Ensure the function handles shifts beyond the end of the alphabet.
   - Example: If the shift results in an index greater than the length of the alphabet, it should wrap around correctly.

3. **Refactoring and Testing**:
   - Test with various inputs to ensure robustness.
   - Validate correct behavior with both regular and edge-case inputs.

### Part 2 - Decryption

#### Objective
- Extend the existing Caesar Cipher program to include functionality for decoding messages.

#### Key Concepts
- **Decoding Process**: Shifting each letter in the ciphertext backward by the specified amount to retrieve the original plaintext.
- **Function Definition**: Creating a `decrypt` function similar to the `encrypt` function.

#### Implementation Steps

1. **Define the `decrypt` Function**:
   - The function takes `cipher_text` and `shift_amount` as parameters.
   - Shift each letter in `cipher_text` backward by `shift_amount`.
   - Print the decoded text.

2. **Handling the `direction` Input**:
   - Check if the user input is "encode" or "decode".
   - Call the corresponding function.

#### Testing the Function
- **Encoding**: 
  - Input: "hello" with shift 5
  - Expected Output: "mjqqt"
- **Decoding**:
  - Input: "mjqqt" with shift 5
  - Expected Output: "hello"

#### Debugging and Edge Cases
- Ensure the decrypt function correctly handles shifts beyond the start of the alphabet.
- Example: Decoding "e" with a shift of 5 should wrap around to "z".

### Part 3 - Reorganizing our code

#### Objective
- Refactor the code to combine the `encrypt` and `decrypt` functions into a single function named `caesar`.

#### Key Concepts
- **Code Simplification**: Reducing code duplication by combining similar functions.
- **Dynamic Functionality**: Using inputs to determine the behavior of a function.

#### Implementation Steps

1. **Define the `caesar` Function**:
   - This function will take three parameters: `start_text`, `shift_amount`, and `cipher_direction`.
   - The function will handle both encryption and decryption based on the value of `cipher_direction`.

2. **Call the `caesar` Function**:
   - Replace the existing calls to `encrypt` and `decrypt` with a single call to `caesar`.

   ```python
   caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
   ```

3. **Remove Redundant Code**:
   - Delete the `encrypt` and `decrypt` functions.
   - Simplify the main code to only call the `caesar` function.

#### Testing and Debugging
- **Testing**: Ensure that encoding and decoding both work correctly.
  - Example: Encoding "hello" with a shift of 5 should result in "mjqqt".
  - Decoding "mjqqt" with a shift of 5 should return "hello".
- **Bug Fix**: Ensure that the adjustment of `shift_amount` based on `cipher_direction` is done outside the loop to avoid repeated modifications.

#### Conclusion
By combining the `encrypt` and `decrypt` functions into a single `caesar` function, we have significantly simplified the code and reduced redundancy. This makes the code easier to maintain and understand.

### Part 4 - UI improvements

We're at the final stage of our Caesar Cipher project. This lesson focuses on enhancing the user experience, fixing bugs, and adding additional functionality to make the program more robust.

#### To-Do List
1. Import and print the logo from `art.py`.
   - First, ensure you have the `art.py` file with an ASCII art logo.
   - Import the `logo` variable from `art.py` and print it when the program starts.
2. Handle large shift values.
   - Use the modulus operator to keep the shift value within the range of 0-25.
3. Preserve non-alphabetical characters.
   - Modify the loop to check if each character is in the alphabet. If not, append it unchanged.
4. Allow the user to restart the cipher program.
   - Use a while loop to repeatedly ask the user if they want to continue using the cipher until they decide to exit.

### Summary
We've completed the Caesar Cipher project by enhancing the code to handle large shift values, preserving non-alphabetical characters, and allowing users to restart the program. This provides a more robust and user-friendly application. You can further customize and expand this program as needed.