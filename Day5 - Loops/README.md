# Day 5 - Python Loops<!-- omit in toc -->

- [Lesson 15 - Using the for loop with Python Lists](#lesson-15---using-the-for-loop-with-python-lists)
  - [Key Concepts](#key-concepts)
    - [For Loop](#for-loop)
    - [Syntax of a For Loop](#syntax-of-a-for-loop)
  - [Example with a List](#example-with-a-list)
  - [Detailed Explanation](#detailed-explanation)
  - [Debugging with Thonny IDE](#debugging-with-thonny-ide)
  - [Extended Example](#extended-example)
  - [Importance of Indentation](#importance-of-indentation)
  - [Practical Application](#practical-application)
- [Practice 1 - Average Height](#practice-1---average-height)
- [Practice 2 - High Score](#practice-2---high-score)
- [Lesson 16 - `for` loops and the `range()` function](#lesson-16---for-loops-and-the-range-function)
  - [Overview](#overview)
  - [Key Concepts](#key-concepts-1)
    - [For Loops Independent of Lists](#for-loops-independent-of-lists)
    - [The `range` Function](#the-range-function)
  - [Basic Usage of `range`](#basic-usage-of-range)
  - [Adjusting the Range](#adjusting-the-range)
  - [Custom Step Size](#custom-step-size)
  - [Practical Example: Summing Numbers from 1 to 100](#practical-example-summing-numbers-from-1-to-100)
  - [Important Points](#important-points)
  - [Conclusion](#conclusion)
- [Practice 3 - Adding even numbers](#practice-3---adding-even-numbers)
- [Practice 4 - Fizzbuzz](#practice-4---fizzbuzz)
- [Project 5: PyPassword Generator](#project-5-pypassword-generator)
  - [Objective](#objective)
  - [Requirements](#requirements)
  - [Functionality](#functionality)
  - [Implementation Steps](#implementation-steps)
  - [Extra Challenge (Optional)](#extra-challenge-optional)
  - [Example Output](#example-output)


## Lesson 15 - Using the for loop with Python Lists

### Key Concepts

#### For Loop
A `for` loop is used to iterate over a sequence (such as a list) and perform actions on each item in the sequence.

#### Syntax of a For Loop
The general syntax of a `for` loop in Python is:
```python
for item in sequence:
    # block of code
```

### Example with a List
We used a list of fruits to demonstrate how a `for` loop works:
```python
fruits = ["apple", "peach", "pear"]

for fruit in fruits:
    print(fruit)
```
This loop iterates through each item in the `fruits` list and prints it out. The expected output is:
```
apple
peach
pear
```

### Detailed Explanation
1. **Initialization**: The `for` loop starts by taking the first item in the list (`apple`).
2. **Assignment**: The variable `fruit` is assigned the value of the current item (`apple`).
3. **Execution**: The code inside the loop (`print(fruit)`) is executed, printing `apple`.
4. **Repetition**: The loop moves to the next item (`peach`), assigns `fruit` to it, and executes the print statement again.
5. **Completion**: This process repeats until all items in the list have been processed.

### Debugging with Thonny IDE
Using the Thonny IDE can help visualize the process:
- **Variables Pane**: Shows the current state of variables.
- **Step-by-Step Execution**: Allows you to see each step of the loop in action, making it clear how the `fruit` variable changes.

### Extended Example
You can include multiple statements within a `for` loop to perform additional actions:
```python
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
```
Expected output:
```
apple
apple Pie
peach
peach Pie
pear
pear Pie
```

### Importance of Indentation
Indentation is crucial in Python, especially in loops and conditional statements. Indented code is considered part of the loop:
```python
for fruit in fruits:
    print(fruit)          # This line is inside the loop
print("Done")             # This line is outside the loop
```
- If a line is inside the loop, it will execute with each iteration.
- If a line is outside the loop, it will execute only once after the loop completes.

### Practical Application
Loops can save time and effort by automating repetitive tasks. For example, instead of manually printing each fruit, a `for` loop can handle it in just a few lines of code.

## Practice 1 - Average Height

You are going to write a program that calculates the average student height from a List of heights.

e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

The average height can be calculated by adding all the heights together and dividing by the total number of heights.

e.g.

180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146

There are a total of **7** heights in student_heights

1146 ÷ 7 = 163.71428571428572

Average height rounded to the nearest whole number = **164**

**Important** You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

**Example Input 1**
```
156 178 165 171 187
```
In this case, student_heights would be a list that looks like: [156, 178, 165, 171, 187]

**Example Output 1**
```
total height = 857
number of students = 5
average height = 171
```
**Example Input 2**
```
151 145 179
```

**Example Output 2**
```
total height = 475
number of students = 3
average height = 158
```

## Practice 2 - High Score

You are going to write a program that calculates the highest score from a List of scores.

e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

Important you are not allowed to use the max or min functions. The output words must match the example. i.e

The highest score in the class is: x

**Example Input**
```
78 65 89 86 55 91 64 89
```
In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]

**Example Output**
```
The highest score in the class is: 91
```

## Lesson 16 - `for` loops and the `range()` function

### Overview
In this lesson, we explored the use of `for` loops with the `range` function in Python. This allows us to iterate over a sequence of numbers without needing a predefined list. This technique is particularly useful for tasks such as summing a series of numbers.

### Key Concepts

#### For Loops Independent of Lists
- **Flexibility**: For loops can be used independently of lists to perform repetitive tasks involving ranges of numbers.
- **Historical Example**: Carl Gauss quickly summed numbers from 1 to 100 by recognizing patterns, which we can emulate using Python.

#### The `range` Function
The `range` function generates a sequence of numbers. The syntax for `range` is:
```python
range(start, stop, step)
```
- **start**: The starting value of the range (inclusive).
- **stop**: The stopping value of the range (exclusive).
- **step**: The increment between each number in the range (optional, defaults to 1).

### Basic Usage of `range`
To print numbers from 1 to 9:
```python
for number in range(1, 10):
    print(number)
```
Output:
```
1
2
3
4
5
6
7
8
9
```
- Note: The range goes up to, but does not include, 10.

### Adjusting the Range
To include the number 10:
```python
for number in range(1, 11):
    print(number)
```
Output:
```
1
2
3
4
5
6
7
8
9
10
```

### Custom Step Size
To use a step size other than 1, specify the step argument. For example, a step size of 3:
```python
for number in range(1, 11, 3):
    print(number)
```
Output:
```
1
4
7
10
```

### Practical Example: Summing Numbers from 1 to 100
Using a `for` loop and the `range` function, we can sum the numbers from 1 to 100:
```python
total = 0
for number in range(1, 101):
    total += number
print(total)
```
Output:
```
5050
```
- **Explanation**: The loop iterates from 1 to 100, adding each number to the `total` variable. The final sum matches Carl Gauss's result of 5050.

### Important Points
- **Efficiency**: Using `range` is efficient for generating sequences of numbers without needing to store them in a list.
- **Syntax Flexibility**: The `range` function can be customized with different start, stop, and step values to suit various needs.

### Conclusion
By understanding and utilizing the `range` function, we can handle repetitive numerical tasks efficiently. Practice using `for` loops with `range` to solidify your understanding and explore further applications in coding exercises.

## Practice 3 - Adding even numbers

You are going to write a program that calculates the sum of all the even numbers from 1 to X. If X is 100 then the first even number would be 2 and the last one is 100:

i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.

Also, we will constrain the inputs to only take numbers from 0 to a **max of 1000**.

**Example Input 1**
```
10
```
**Example Output 1**
```
30
```
**Example Input 2**
```
52
```
**Example Output 2**
```
702
```
**Hint**

There are quite a few ways of solving this problem, but you will need to use the range() function in any of the solutions.

## Practice 4 - Fizzbuzz

You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:

- Your program should print each number from 1 to 100 in turn and include number 100.
- When the number is divisible by 3 then instead of printing the number it should print "Fizz".
- When the number is divisible by 5, then instead of printing the number it should print "Buzz".
- And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

e.g. it might start off like this:

```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
...etc
```

**Hint**

- Remember your answer should start from 1 and go up to and including 100.
- Each number/text should be printed on a separate line.

## Project 5: PyPassword Generator

[Demo](https://appbrewery.github.io/python-day5-demo/)

### Objective
The objective of this project is to develop a Python-based password generator, named PyPassword, that can create secure and random passwords based on user-defined criteria. The generated passwords will include a mix of letters, symbols, and numbers, making them highly secure and difficult to crack.

### Requirements

1. **User Inputs**:
    - The number of letters in the password.
    - The number of symbols in the password.
    - The number of numbers in the password.

2. **Password Components**:
    - **Letters**: A-Z (uppercase) and a-z (lowercase).
    - **Symbols**: A predefined set of symbols typically accepted in passwords.
    - **Numbers**: 0-9.

3. **Password Generation**:
    - **Easy Level**: Generate a password where letters, symbols, and numbers appear in sequence. For example, if the user requests 4 letters, 2 symbols, and 2 numbers, the password might look like `abcd!@12`.
    - **Hard Level**: Generate a password where the letters, symbols, and numbers appear in a completely random order. For example, if the user requests 4 letters, 2 symbols, and 2 numbers, the password might look like `a!b2c@3d`.

### Functionality

1. **Input Handling**:
    - Prompt the user to enter the number of letters, symbols, and numbers they want in their password.
    - Validate the inputs to ensure they are positive integers.

2. **Password Construction**:
    - Use the provided lists of letters, symbols, and numbers.
    - Utilize Python’s `random` module to randomly select characters from these lists.
    - Append the selected characters to form the password based on user specifications.

3. **Output**:
    - Display the generated password to the user.
    - Ensure the password meets the specified criteria (length and composition).

### Implementation Steps

1. **Setup**:
    - Import the `random` module.
    - Define the lists for letters (both uppercase and lowercase), symbols, and numbers.

2. **User Input**:
    - Prompt the user for the number of letters, symbols, and numbers.
    - Store these values.

3. **Password Generation - Easy Level**:
    - Create an empty string or list to build the password.
    - Use loops to append the required number of letters, symbols, and numbers to the password string/list.
    - Concatenate the components to form the final password in sequence.

4. **Password Generation - Hard Level**:
    - Create a list to hold the password components.
    - Append the required number of letters, symbols, and numbers to the list.
    - Shuffle the list to ensure random order.
    - Convert the list back to a string to form the final password.

5. **Display the Password**:
    - Print the generated password to the user.

### Extra Challenge (Optional)

- Implement additional features such as:
    - Allowing users to specify if they want to include/exclude certain characters (e.g., only lowercase letters, no special symbols).
    - Enhancing the UI/UX with a graphical interface using libraries like Tkinter.
    - Providing an option to generate multiple passwords at once.

### Example Output

For a user input of 4 letters, 2 symbols, and 2 numbers:

- **Easy Level**: `AbCd!@12`
- **Hard Level**: `A1b!C@d2`

By completing this project, you will gain a deeper understanding of loops, randomization, user input handling, and list manipulation in Python. This exercise will also demonstrate the practical application of these concepts in creating secure and user-friendly software.