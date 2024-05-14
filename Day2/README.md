# Day 2 - Understanding Data Types and How to Manipulate Strings<!-- omit in toc -->

- [Lesson 5 - Introduction to Data Types in Python](#lesson-5---introduction-to-data-types-in-python)
  - [Key Data Types in Python](#key-data-types-in-python)
  - [Working with Data Types](#working-with-data-types)
  - [Errors and Type Limitations](#errors-and-type-limitations)
  - [Practical Applications](#practical-applications)
  - [Understanding Functions, Type Errors, and Type Conversion in Python](#understanding-functions-type-errors-and-type-conversion-in-python)
    - [Introduction](#introduction)
    - [Functions and Data Types](#functions-and-data-types)
    - [Managing Type Errors](#managing-type-errors)
    - [Practical Example of Type Conversion](#practical-example-of-type-conversion)
    - [Discussion on Other Conversions](#discussion-on-other-conversions)
  - [Practice 1](#practice-1)
    - [Example 1](#example-1)
      - [Input](#input)
      - [Output](#output)
    - [Example 2](#example-2)
      - [Input](#input-1)
      - [Output](#output-1)
    - [Explanation](#explanation)
- [Lesson 6 - Mathematical Operations and Order of Operations in Python](#lesson-6---mathematical-operations-and-order-of-operations-in-python)
  - [Basic Mathematical Operators](#basic-mathematical-operators)
  - [Order of Operations](#order-of-operations)
  - [Examples of Order of Operations](#examples-of-order-of-operations)
  - [Changing the Order Using Parentheses](#changing-the-order-using-parentheses)
  - [Challenge: Modifying the Expression](#challenge-modifying-the-expression)
  - [Practice 2](#practice-2)
    - [Example 1](#example-1-1)
      - [Input](#input-2)
      - [Output](#output-2)
    - [Example 2](#example-2-1)
      - [Input](#input-3)
      - [Output](#output-3)
- [Lesson 7 - Number Manipulation and F Strings in Python](#lesson-7---number-manipulation-and-f-strings-in-python)
  - [Key Concepts](#key-concepts)
  - [Coding Challenge](#coding-challenge)
    - [Solution](#solution)
    - [Explanation of the Code](#explanation-of-the-code)
    - [Testing the Program](#testing-the-program)
  - [Practice 3](#practice-3)
    - [Example Input](#example-input)
    - [Example Output](#example-output)
- [Day 2 Project: Tip Calculator](#day-2-project-tip-calculator)

## Lesson 5 - Introduction to Data Types in Python

### Key Data Types in Python

1. **Strings**:
   - A sequence of characters enclosed within double quotes ("") or single quotes ('').
   - Example:
     ```python
     greeting = "Hello"
     ```

2. **Integers**:
   - Whole numbers without any decimal points.
   - Represented as is, without any quotes.
   - Example:
     ```python
     age = 25
     ```

3. **Floats**:
   - Numbers with decimal points, known as floating-point numbers.
   - Example:
     ```python
     pi = 3.14159
     ```

4. **Booleans**:
   - Represents one of two values: `True` or `False`.
   - These values are used to evaluate conditions and are written with a capital initial letter, without quotes.
   - Example:
     ```python
     is_valid = True
     ```

### Working with Data Types

1. **Length of Strings**:
   - The `len()` function returns the number of characters in a string.
   - Example:
     ```python
     length = len("Hello")  # Outputs 5
     ```

2. **Subscripting Strings**:
   - Access specific characters in a string using square brackets `[]` with an index that starts at 0.
   - Example:
     ```python
     first_letter = "Hello"[0]  # Outputs 'H'
     ```

3. **Concatenating Strings**:
   - Strings can be combined using the `+` operator.
   - Example:
     ```python
     full_greeting = "Hello" + " " + "World"  # Outputs 'Hello World'
     ```

4. **Mathematical Operations on Integers and Floats**:
   - Integers and floats can participate in mathematical operations like addition, subtraction, multiplication, etc.
   - Example:
     ```python
     result = 123 + 345  # Outputs 468
     ```

5. **Visualizing Large Numbers**:
   - Python allows underscores in integers for better readability, which the interpreter ignores.
   - Example:
     ```python
     population = 1_000_000  # Equivalent to 1000000
     ```

### Errors and Type Limitations

- **Type Errors**:
  - Occur when an operation is applied to an inappropriate data type, such as using `len()` on an integer.
  - Example:
    ```python
    # This will raise an error because len() expects a string, not an integer.
    num_length = len(123)
    ```

### Practical Applications

- **Use of Data Types in Conditions**:
  - Booleans are extensively used in control flow statements (if, while) to direct program execution.
- **Type Conversion**:
  - Sometimes it’s necessary to convert data types, like converting a string to an integer for mathematical operations or vice versa.

### Understanding Functions, Type Errors, and Type Conversion in Python

#### Introduction
In this lesson, we'll explore how functions in Python handle data types and how to manage type errors through type conversion. Understanding these concepts is essential for writing robust Python code.

#### Functions and Data Types

1. **Function Analogies**:
   - Think of functions as machines in a factory that take specific types of inputs (data types) and produce a certain type of output. Just like a machine designed to process potatoes can't handle rocks, functions in Python are designed to work with specific data types.

2. **Type Errors in Functions**:
   - When a function receives data of a type it doesn't expect, it results in a Type Error. For example, the `len()` function expects a string or other sequence type and will throw an error if given an integer:
     ```python
     print(len(123))  # TypeError: object of type 'int' has no len()
     ```

#### Managing Type Errors

1. **Using the `type()` Function**:
   - You can check the data type of a variable using the `type()` function, which helps in debugging and understanding what type of data you are dealing with.
   - Example:
     ```python
     my_var = "Hello"
     print(type(my_var))  # <class 'str'>
     ```

2. **Type Conversion (Type Casting)**:
   - Python allows you to convert data from one type to another, which is useful when you need to perform operations that require specific data types.
   - Common type conversion functions include `str()`, `int()`, and `float()`.

#### Practical Example of Type Conversion

1. **Concatenating Strings with Numbers**:
   - Concatenating a string with a number directly will result in a TypeError. To concatenate them, convert the number to a string first:
     ```python
     age = 30
     message = "You are " + str(age) + " years old."
     print(message)
     ```

2. **Changing Data Types**:
   - You can convert a numeric string into an integer or float, which is useful for performing mathematical operations:
     ```python
     num_string = "100"
     num_int = int(num_string)
     print(num_int + 50)  # 150
     ```

#### Discussion on Other Conversions

1. **From Integer to Float and Vice Versa**:
   - Convert integers to floats when you need to perform operations that produce fractional results. Similarly, convert floats to integers if you need a whole number result.
   - Example:
     ```python
     float_num = float(100)  # Converts integer 100 to float 100.0
     int_num = int(100.5)    # Converts float to integer, truncating to 100
     ```

2. **Complex Conversions**:
   - Python also allows for more complex conversions such as converting between different bases (binary, hexadecimal, etc.) but these are more advanced and will be covered later.

### Practice 1

Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

The last line of your program should print the result.

#### Example 1 
##### Input
```39```

##### Output
```12```

#### Example 2 
##### Input
```43```

##### Output
```7```

#### Explanation
1. **Input**: The `input()` function captures the user's input as a string.
2. **String Indexing**: The `two_digit_number[0]` retrieves the first character, and `two_digit_number[1]` retrieves the second character.
3. **Type Conversion**: The `int()` function converts the string characters to integers.
4. **Addition**: The two integers are added together.
5. **Output**: The `print()` function displays the result.

## Lesson 6 - Mathematical Operations and Order of Operations in Python

### Basic Mathematical Operators
1. **Addition (`+`)**: Adds two numbers or concatenates two strings.
   ```python
   result = 7 + 3    # 10
   ```

2. **Subtraction (`-`)**: Subtracts the second number from the first.
   ```python
   result = 7 - 3    # 4
   ```

3. **Multiplication (`*`)**: Multiplies two numbers.
   ```python
   result = 3 * 2    # 6
   ```

4. **Division (`/`)**: Divides the first number by the second. Always returns a float.
   ```python
   result = 6 / 3    # 2.0
   ```

5. **Exponentiation (`**`)**: Raises the first number to the power of the second.
   ```python
   result = 2 ** 3   # 8
   ```

### Order of Operations
Python follows the PEMDAS rule to determine the order in which operations are performed. When multiple operations occur on the same line, Python processes them in the following order:
1. **Parentheses**: Operations inside parentheses are performed first.
2. **Exponents**: Next, exponentiation is performed.
3. **Multiplication and Division**: These operations are processed from left to right.
4. **Addition and Subtraction**: Finally, addition and subtraction are performed from left to right.

### Examples of Order of Operations
Let's consider the example provided:
```python
result = 3 * 3 + 3 / 3 - 3
print(result)  # Output: 7.0
```

**Step-by-Step Evaluation**:
1. **Multiplication**: \(3 * 3 = 9\)
2. **Division**: \(3 / 3 = 1.0\)
3. **Addition**: \(9 + 1.0 = 10.0\)
4. **Subtraction**: \(10.0 - 3 = 7.0\)

The final result is `7.0`.

### Changing the Order Using Parentheses
You can change the order of operations by using parentheses to group operations:
```python
result = 3 * (3 + 3) / 3 - 3
print(result)  # Output: 3.0
```

**Step-by-Step Evaluation**:
1. **Parentheses**: \(3 + 3 = 6\)
2. **Multiplication**: \(3 * 6 = 18\)
3. **Division**: \(18 / 3 = 6.0\)
4. **Subtraction**: \(6.0 - 3 = 3.0\)

The final result is `3.0`.

### Challenge: Modifying the Expression
To change the original expression `3 * 3 + 3 / 3 - 3` so that it evaluates to `3` using parentheses, you can adjust the order of operations:

**Original Expression**:
```python
result = 3 * 3 + 3 / 3 - 3
print(result)  # Output: 7.0
```

**Modified Expression**:
```python
result = 3 * (3 + 3) / 3 - 3
print(result)  # Output: 3.0
```

By adding parentheses around `3 + 3`, you ensure that the addition operation is performed first, followed by multiplication, division, and subtraction.

### Practice 2

Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

[BMI Wikipedia Page](https://en.wikipedia.org/wiki/Body_mass_index)

The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

$BMI= \dfrac{weight(kg)}{height^2(m^2)}$

NOTE: You should convert the bmi to a whole number and print out a whole number in order to pass all the tests. See examples below.

#### Example 1
##### Input
```
1.75
80
```
means: weight = 80 and height = 1.75
##### Output
```
26
```
Since: 80 ÷ (1.75 x 1.75) = 26.122448979591837

#### Example 2
##### Input
```
1.58
57
```
##### Output
```
22
```

## Lesson 7 - Number Manipulation and F Strings in Python

### Key Concepts

1. **Rounding Numbers**:
   - `round(number)`: Rounds a number to the nearest integer.
   - `round(number, ndigits)`: Rounds a number to a specified number of decimal places.
   ```python
   print(round(8 / 3))  # Outputs: 3
   print(round(8 / 3, 2))  # Outputs: 2.67
   ```

2. **Floor Division**:
   - `//`: Divides two numbers and returns the largest integer less than or equal to the result.
   ```python
   print(8 // 3)  # Outputs: 2
   ```

3. **Compound Assignment Operators**:
   - `+=`, `-=`, `*=`, `/=`: Shorthand for updating the value of a variable based on its current value.
   ```python
   score = 0
   score += 1  # Equivalent to score = score + 1
   print(score)  # Outputs: 1
   ```

4. **F-strings**:
   - F-strings provide a way to embed expressions inside string literals, using curly braces `{}`.
   ```python
   score = 0
   height = 1.8
   isWinning = True
   print(f"Your score is {score}, your height is {height}, you are winning: {isWinning}")
   # Outputs: Your score is 0, your height is 1.8, you are winning: True
   ```

### Coding Challenge

Now, let's create a program that utilizes these concepts. The goal is to take two inputs from the user: a number and the number of decimal places to round it to. The program will print the rounded number using an F-string.

Here are the steps:

1. Get the number from the user.
2. Get the number of decimal places to round to from the user.
3. Round the number to the specified number of decimal places.
4. Print the result using an F-string.

#### Solution

```python
# Step 1: Get the number from the user
number = float(input("Enter a number: "))

# Step 2: Get the number of decimal places to round to
decimal_places = int(input("Enter the number of decimal places to round to: "))

# Step 3: Round the number
rounded_number = round(number, decimal_places)

# Step 4: Print the result using an F-string
print(f"The number {number} rounded to {decimal_places} decimal places is {rounded_number}")
```

#### Explanation of the Code

1. **Input Handling**:
   - `float(input("Enter a number: "))`: Reads a number from the user and converts it to a float.
   - `int(input("Enter the number of decimal places to round to: "))`: Reads an integer from the user, specifying the number of decimal places.

2. **Rounding**:
   - `round(number, decimal_places)`: Rounds the number to the specified number of decimal places.

3. **Output**:
   - The result is printed using an F-string, which embeds the variables directly into the string for clear and readable output.

#### Testing the Program

You can test the program with different inputs to ensure it works correctly. Here are a few test cases:

- **Test Case 1**:
  - Number: 8.666666
  - Decimal Places: 2
  - Expected Output: The number 8.666666 rounded to 2 decimal places is 8.67

- **Test Case 2**:
  - Number: 3.14159
  - Decimal Places: 3
  - Expected Output: The number 3.14159 rounded to 3 decimal places is 3.142

- **Test Case 3**:
  - Number: 2.71828
  - Decimal Places: 1
  - Expected Output: The number 2.71828 rounded to 1 decimal place is 2.7

By running the program with these inputs, you can verify that it correctly rounds the numbers and outputs them as expected.

### Practice 3

I was reading this article by Tim Urban - [Your Life in Weeks](https://waitbutwhy.com/2014/05/life-weeks.html) and realised just how little time we actually have.

Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

You have x weeks left.
Where x is replaced with the actual calculated number of weeks the input age has left until age 90.

#### Example Input
```
56
```
#### Example Output
```
You have 1768 weeks left.
```

## Day 2 Project: Tip Calculator

If the bill was $150.00, split between 5 people, with 12% tip. 

Each person should pay (150.00 / 5) * 1.12 = 33.6
Format the result to 2 decimal places = 33.60

Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪