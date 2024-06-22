# Day 3 - Control Flow and Logical Operators<!-- omit in toc -->

- [Lesson 8 - Control Flow with `if`/`else` and Conditional Operators](#lesson-8---control-flow-with-ifelse-and-conditional-operators)
  - [Introduction to Conditionals](#introduction-to-conditionals)
  - [The Overflow Mechanism Analogy](#the-overflow-mechanism-analogy)
  - [Python Conditional Statements](#python-conditional-statements)
  - [Example: Rollercoaster Height Check](#example-rollercoaster-height-check)
  - [Indentation in Python](#indentation-in-python)
  - [Comparison Operators](#comparison-operators)
  - [Practical Application](#practical-application)
  - [Notes on Equal Signs](#notes-on-equal-signs)
- [Practice 1 - Odd or Even](#practice-1---odd-or-even)
- [Lesson 9 - Nested if statements and elif statements](#lesson-9---nested-if-statements-and-elif-statements)
  - [Introduction to Nested If/Else Statements](#introduction-to-nested-ifelse-statements)
  - [Concept of Nested If/Else Statements](#concept-of-nested-ifelse-statements)
  - [Implementation in Python](#implementation-in-python)
  - [Introduction to Elif Statements](#introduction-to-elif-statements)
    - [Concept of Elif Statements](#concept-of-elif-statements)
  - [Implementation with Elif in Python](#implementation-with-elif-in-python)
  - [Additional Notes on Elif Statements](#additional-notes-on-elif-statements)
- [Practice 2 - BMI Calculator 2.0](#practice-2---bmi-calculator-20)
- [Practice 3 - Leap Year](#practice-3---leap-year)
- [Lesson 10 -  Multiple If Statements in Succession](#lesson-10----multiple-if-statements-in-succession)
  - [Recap: If/Elif/Else Statements](#recap-ifelifelse-statements)
  - [Checking Multiple Independent Conditions](#checking-multiple-independent-conditions)
  - [Implementing Multiple Independent Conditions](#implementing-multiple-independent-conditions)
  - [Key Points](#key-points)
  - [Shortening Increment Operations](#shortening-increment-operations)
  - [Practical Implementation](#practical-implementation)
  - [Conceptual Understanding](#conceptual-understanding)
- [Practice 4 - Pizza order](#practice-4---pizza-order)
- [Lesson 11 - Logical Operators](#lesson-11---logical-operators)
  - [Using `and` Operator](#using-and-operator)
  - [Using `or` Operator](#using-or-operator)
  - [Using `not` Operator](#using-not-operator)
  - [Practical Example: Enhanced Rollercoaster Ticketing System](#practical-example-enhanced-rollercoaster-ticketing-system)
  - [Updated Code with Logical Operators](#updated-code-with-logical-operators)
  - [Explanation](#explanation)
  - [Key Points](#key-points-1)
- [Practice 5 - Love Calculator](#practice-5---love-calculator)
- [Project 3 - Treasure Island / "Choose Your Own Adventure" Game](#project-3---treasure-island--choose-your-own-adventure-game)
  - [Overview](#overview)
  - [Objectives](#objectives)
  - [Requirements](#requirements)
  - [Deliverables](#deliverables)
  - [Evaluation Criteria](#evaluation-criteria)


## Lesson 8 - Control Flow with `if`/`else` and Conditional Operators

### Introduction to Conditionals
- **Context**: Real-world analogy using a bathtub overflow mechanism to explain conditional statements.
- **Purpose**: Conditionally execute code based on whether a specified condition is met.

### The Overflow Mechanism Analogy
- **Bathtub Example**: Prevents overflow using an overflow drain.
  - **Conditional Statement**:
    - If water level > 80 cm: drain water.
    - Else: continue filling tub.
  
### Python Conditional Statements
- **Syntax**:
  ```python
  if condition:
      # code block executed if condition is true
  else:
      # code block executed if condition is false
  ```
- **Key Elements**:
  - **`if` keyword**: Introduces the condition.
  - **Condition**: Expression evaluated to `True` or `False`.
  - **Colon (`:`)**: Follows the condition.
  - **Indented Code Block**: Executed if the condition is true.
  - **`else` keyword**: Executes alternative code block if the condition is false.

### Example: Rollercoaster Height Check
- **Problem**: Only allow people taller than 120 cm to buy a ticket.
- **Flowchart**: Represents the logic of the height check.
- **Code Implementation**:
  ```python
  print("Welcome to the rollercoaster!")
  height = int(input("Enter your height in cm: "))

  if height > 120:
      print("You can ride the rollercoaster!")
  else:
      print("Sorry, you have to grow taller before you can ride.")
  ```

### Indentation in Python
- **Importance**: Indicates the block of code under `if` and `else`.
- **Error Handling**: Incorrect indentation results in an `IndentationError`.

### Comparison Operators
- **Greater Than**: `>`
  - Example: `height > 120`
- **Greater Than or Equal To**: `>=`
  - Includes the value itself (e.g., `height >= 120`).
- **Other Operators**:
  - **Less Than**: `<`
  - **Less Than or Equal To**: `<=`
  - **Equal To**: `==`
  - **Not Equal To**: `!=`

### Practical Application
- **Repl.it Implementation**: Test the height check in an interactive environment.
  - **Input Handling**: Convert user input to integer for comparison.
  - **Conditional Execution**: Print messages based on the user's height.

### Notes on Equal Signs
- **Assignment (`=`)**: Assigns a value to a variable.
  - Example: `height = 120`
- **Equality Check (`==`)**: Compares two values.
  - Example: `height == 120`
- **Common Mistake**: Using `=` instead of `==` in conditions.

## Practice 1 - Odd or Even

Write a program that works out whether if a given number is an odd or even number.

Even numbers can be divided by 2 with no remainder.

e.g. 86 is even because 86 ÷ 2 = 43

43 does not have any decimal places. Therefore the division is clean.

e.g. 59 is odd because 59 ÷ 2 = 29.5

29.5 is not a whole number, it has decimal places. Therefore there is a remainder of 0.5, so the division is not clean.

> The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.

e.g.

6 ÷ 2 = 3 with no remainder.

therefore: 6 % 2 = 0

5 ÷ 2 = 2 x 2 + 1, remainder is 1.

therefore: 5 % 2 = 1

14 ÷ 4 = 3 x 4 + 2, remainder is 2.

therefore: 14 % 4 = 2


**Example 1 Input**
```
43
```
**Example 1 Output**
```
This is an odd number.
```

**Example 2 Input**
```
94
```
**Example 2 Output**
```
This is an even number.
```

## Lesson 9 - Nested if statements and elif statements

### Introduction to Nested If/Else Statements
- **Scenario**: Adding an additional condition (age) to the existing height check for purchasing a rollercoaster ticket. [Flow Chart](https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Rollercoaster%202#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1J7_rw1flGeF0hmc_zrMzPX7t6xkbcsiX%26export%3Ddownload#%7B%22pageId%22%3A%22bzYDor7Mf7Ch-uxfBpj_%22%7D)
- **Problem**: Determine ticket price based on age:
  - Over 18 years: $12
  - 18 years or under: $7

### Concept of Nested If/Else Statements
- **Structure**: An if/else statement inside another if statement.
- **Purpose**: Allows multiple conditions to be checked in a sequence.
- **[Flowchart](https://viewer.diagrams.net/?target=blank&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Rollercoaster%202#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1XaUDMIKOxCUzJbsuZevgHZmgKr7rICbI%26export%3Ddownload#%7B%22pageId%22%3A%22bzYDor7Mf7Ch-uxfBpj_%22%7D)**: Visual representation of nested conditions.
  - Check if height > 120 cm:
    - If yes, check age.
    - If age ≤ 18: ticket price $7.
    - If age > 18: ticket price $12.
  - If no: Cannot ride.

### Implementation in Python
1. **Initial Height Check**:
   ```python
   if height > 120:
       # Nested if/else for age check
   else:
       print("Sorry, you have to grow taller before you can ride.")
   ```

2. **Adding Age Check**:
   ```python
   if height > 120:
       age = int(input("What is your age? "))
       if age <= 18:
           print("Ticket price is $7.")
       else:
           print("Ticket price is $12.")
   ```

### Introduction to Elif Statements
- **Scenario Expansion**: More detailed pricing tiers based on age:
  - Less than 12 years: $5
  - Between 12 and 18 years: $7
  - Over 18 years: $12

#### Concept of Elif Statements
- **Structure**: Combines multiple conditions in a single if/else block.
- **Purpose**: Simplifies checking several conditions sequentially.
- **Syntax**:
  ```python
  if condition1:
      # code block if condition1 is true
  elif condition2:
      # code block if condition2 is true
  else:
      # code block if none of the above conditions are true
  ```

### Implementation with Elif in Python
1. **Initial Height Check with Nested Age Check**:
   ```python
   if height > 120:
       age = int(input("What is your age? "))
       if age < 12:
           print("Ticket price is $5.")
       elif age <= 18:
           print("Ticket price is $7.")
       else:
           print("Ticket price is $12.")
   else:
       print("Sorry, you have to grow taller before you can ride.")
   ```

2. **Explanation**:
   - The first `if` checks if height is greater than 120 cm.
   - The nested conditions check age:
     - If age < 12, print $5 ticket price.
     - Elif age ≤ 18, print $7 ticket price.
     - Else, print $12 ticket price.
   - The outer `else` handles cases where height is 120 cm or less.

### Additional Notes on Elif Statements
- **Flexibility**: Add as many `elif` conditions as necessary.
- **Example**:
  ```python
  if condition1:
      # code for condition1
  elif condition2:
      # code for condition2
  elif condition3:
      # code for condition3
  else:
      # code if none of the conditions are true
  ```

## Practice 2 - BMI Calculator 2.0

Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Equal to or over 18.5 but below 25 they have a normal weight
Equal to or over 25 but below 30 they are slightly overweight
Equal to or over 30 but below 35 they are obese
Equal to or over 35 they are clinically obese.

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

$BMI= \dfrac{weight(kg)}{height^2(m^2)}$

**Important**: you do not need to round the result to the nearest whole number. It's fine to print out a floating point number for this exercise. The interpretation message needs to include the words from the interpretations above. e.g. underweight, normal weight, overweight, obese, clinically obese.

**Example Input 1**
```
1.50
63
```
**Example Output 1**
```
Your BMI is 28.0, you are slightly overweight.
```

since 63 ÷ (1.50 x 1.50) = 28

The testing code will check for print output that is formatted like one of the lines below:

```
Your BMI is 18.28678, you are underweight.

Your BMI is 22.0, you have a normal weight.

Your BMI is 28.50752, you are slightly overweight.

Your BMI is 32.56189, you are obese.

Your BMI is 37.50000, you are clinically obese.
```

**Example Input 2**
```
1.60
96
```
**Example Output 2**
```
Your BMI is 37.49999999999999, you are clinically obese.
```

**Example Input 3**
```
1.71
73
```
**Example Output 3**
```
Your BMI is 24.96494647925858, you have a normal weight.
```


## Practice 3 - Leap Year

💪 This is a difficult challenge! 💪

Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, [this video](https://www.youtube.com/watch?v=xX96xng7sAE) does it more justice.

This is how you work out whether if a particular year is a leap year.

on every year that is divisible by 4 with no remainder

except every year that is evenly divisible by 100 with no remainder

unless the year is also divisible by 400 with no remainder

If english is not your first language or if the above logic is confusing, try using [this flow chart](https://viewer.diagrams.net/index.html?target=blank&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Leap%20Algorithm#R7VpNc9owEP01HNuxJdmYY4CkzTTNdEpmmhyFrdhqhcXIIkB%2BfSUsY4wcQhqwC%2B0p0urDu29Xu08KHTiYLD4JPE2%2B8oiwDnCiRQcOOwC4CPjqj5Ysc0k3gLkgFjQyk0rBiD4TI3SMdEYjklUmSs6ZpNOqMORpSkJZkWEh%2BLw67ZGz6lenOCaWYBRiZkt/0EgmuTQA3VL%2BmdA4Kb7s%2Br18ZIKLycaSLMERn2%2BI4GUHDgTnMm9NFgPCNHgFLvm6qxdG14oJksp9FoDbYTJlQFxPomj0Jbzr4tT9YJTN5LIwmETKftPlQiY85ilml6W0L/gsjYje1VG9cs4N51MldJXwJ5FyaZyJZ5IrUSInzIwqhcXyXq//6BXdB7PdqjNcVHpL08t11Qq%2BCIERZXwmQrLD7iKUsIiJ3DEPrB2lIpzwCVH6qHWCMCzpU1UPbEItXs8rvaEaxiFvcI7Z9wmzmfnS6O7i%2B53lstIhGt15QiUZTfHK/rk6lVXwzZ5ESLLYDaNttlkAYE85brVoWZxWE%2BTz8oy4xRFONs4Hco6ElfePBjLYM5DhOwN5tfRCCLzcmDDlNJXZxs7ftKAMFLcLtgKlyOulq/M9S8evlfvzWPD/x8LOWHCdQwSD5W3kdre97W8d91w1s64Mg7fGFQLWl5qIK2Dl4%2BtMr9GahYzglGkjOsBnCv3%2BWKhWrFsRfaIZHas4A85YT0EdeGVn8YRPxrOsmQxe8Jcif3dr8jf07PwdHCt/QwvbW65xvSHK/HcVvEfK2IAzLlZr4WMQkjBU8kwK/otsjIwDD3nOYQB23SrA65PQWoHs1gBsAasMllX0MKNxqtqhMpwooPoaFqr48YUZmNAoyjMoyegzHq%2B20iiaQ6z29fodb6j3Ukkzy/PngeLYDSwm0rOBhjU4g2PhHFg4P5Ds5IGG/j5AoyaBdmErZX5B5X1RyFX7oaz4qlfWeN0pSvxfQA2KVPM6N2j3xhO06VP3XH2KWvWpcyjapG%2BZLRMn6IPX63pdvTkacXJtVnpwzhR5JIhQHWcKwBj6/oFIqVfFFtaR0kY5E2jnVeFESwzaMx2BVtMRaOd14ERLzL4%2BdXutlhh0qBKD2i8xyNum2rWJsI5rH6/I9M6lyHi9bXRRzUWm4TJjM6RzuDOi3hZXClq%2BMRYmnNcbCHS3I7oO6EbfQIDNSc8AaGQBDdt%2BbAL2s%2Bk5ZA47Sdch3WzusCnGST9QQ9RkHVTd8ocO%2Bb9jyp%2BLwMvf#%7B%22pageId%22%3A%22QVN9pPIG4B-1iTNCvefn%22%7D) .

e.g. The year 2000:

2000 ÷ 4 = 500 (Leap)

2000 ÷ 100 = 20 (Not Leap)

2000 ÷ 400 = 5 (Leap!)

So the year 2000 is a leap year.

But the year 2100 is not a leap year because:

2100 ÷ 4 = 525 (Leap)

2100 ÷ 100 = 21 (Not Leap)

2100 ÷ 400 = 5.25 (Not Leap)

Warning your output should match the Example Output format exactly, including spelling an punctuation.

**Example Input 1**
```
2400
```
**Example Output 1**
```
Leap year
```
**Example Input 2**
```
1989
```
**Example Output 2**
```
Not leap year
```

## Lesson 10 -  Multiple If Statements in Succession

### Recap: If/Elif/Else Statements
- **Purpose**: Check multiple conditions to determine ticket price based on age.
- **Syntax**:
  ```python
  if height > 120:
      age = int(input("What is your age? "))
      if age < 12:
          print("Ticket price is $5.")
      elif age <= 18:
          print("Ticket price is $7.")
      else:
          print("Ticket price is $12.")
  else:
      print("Sorry, you have to grow taller before you can ride.")
  ```

### Checking Multiple Independent Conditions
- **Scenario**: Adding a photo option for an additional $3.
- **Concept**:
  - Use separate `if` statements for independent conditions.
  - Each condition is checked regardless of previous conditions' outcomes.
  - Example: Check height and age for ticket price, then check if they want a photo.
  - [Flow chart](https://viewer.diagrams.net/?target=blank&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Rollercoaster%204#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1aoRTeFOb2SJO7ofMnhTCneCEboHowF2A%26export%3Ddownload#%7B%22pageId%22%3A%22bzYDor7Mf7Ch-uxfBpj_%22%7D)

### Implementing Multiple Independent Conditions
- **Example**:
  ```python
  if height > 120:
      age = int(input("What is your age? "))
      if age < 12:
          bill = 5
      elif age <= 18:
          bill = 7
      else:
          bill = 12

      wants_photo = input("Do you want a photo taken? Type Y for yes or N for no. ")
      if wants_photo == 'Y':
          bill += 3

      print(f"Your final bill is ${bill}")
  else:
      print("Sorry, you have to grow taller before you can ride.")
  ```

### Key Points
- **Multiple `if` Statements**: Each `if` statement is evaluated independently.
- **Indentation**:
  - Ensure the second `if` statement (for photo) is at the same indentation level as the first `if` block.
  - Correct indentation determines which block of code gets executed based on conditions.

### Shortening Increment Operations
- **Increment Syntax**:
  ```python
  bill = bill + 3  # Can be shortened to:
  bill += 3
  ```
  
### Practical Implementation
- **Creating a Variable for Bill**:
  - Initialize `bill` to zero.
  - Adjust `bill` based on age.
  - Add photo cost if applicable.
- **Example with Detailed Steps**:
  ```python
  if height > 120:
      age = int(input("What is your age? "))
      bill = 0

      if age < 12:
          bill = 5
      elif age <= 18:
          bill = 7
      else:
          bill = 12

      wants_photo = input("Do you want a photo taken? Type Y for yes or N for no. ")
      if wants_photo == 'Y':
          bill += 3

      print(f"Your final bill is ${bill}")
  else:
      print("Sorry, you have to grow taller before you can ride.")
  ```

### Conceptual Understanding
- **Flowchart Comparison**:
  - `if/elif/else` structure allows only one path (A, B, or C).
  - Multiple independent `if` statements check all relevant conditions.

## Practice 4 - Pizza order

Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.

Based on a user's order, work out their final bill.

Small pizza (S): $15

Medium pizza (M): $20

Large pizza (L): $25

Add pepperoni for small pizza (Y or N): +$2

Add pepperoni for medium or large pizza (Y or N): +$3

Add extra cheese for any size pizza (Y or N): +$1

**Example Input**
```
L
Y
N
```
**Example Output**
```
Thank you for choosing Python Pizza Deliveries!
Your final bill is: $28.
```

## Lesson 11 - Logical Operators

- **Purpose**: Combine multiple conditions in the same line of code.
- **Key Operators**:
  - `and`: Both conditions must be true for the entire expression to be true.
  - `or`: At least one condition must be true for the entire expression to be true.
  - `not`: Reverses the condition's truth value.

### Using `and` Operator
- **Concept**: Ensures that both conditions are true.
- **Syntax**:
  ```python
  A = 12
  print(A > 10 and A < 13)  # True because both conditions are true
  print(A > 15 and A < 13)  # False because the first condition is false
  ```

### Using `or` Operator
- **Concept**: Ensures that at least one condition is true.
- **Syntax**:
  ```python
  A = 12
  print(A > 10 or A < 10)  # True because the first condition is true
  print(A > 15 or A < 10)  # False because both conditions are false
  ```

### Using `not` Operator
- **Concept**: Reverses the condition's truth value.
- **Syntax**:
  ```python
  A = 12
  print(not A > 15)  # True because A > 15 is false
  ```

### Practical Example: Enhanced Rollercoaster Ticketing System
- **Scenario**: Add a special price category for people aged between 45 and 55 (mid life crisis), giving them free tickets.
- **Steps**:
  1. **Current Conditions**: 
     - Age < 12: $5
     - 12 <= Age <= 18: $7
     - Age > 18: $12
  2. **Add New Condition**: 
     - 45 <= Age <= 55: Free ticket
  3. **Check for Additional Option**: Ask if they want a photo for an additional $3.

### Updated Code with Logical Operators
```python
height = int(input("What is your height in cm? "))

if height > 120:
    age = int(input("What is your age? "))
    bill = 0

    if age < 12:
        bill = 5
    elif 12 <= age <= 18:
        bill = 7
    elif 45 <= age <= 55:
        print("Everything's going to be ok. Have a free ride on us!")
    else:
        bill = 12

    if age < 45 or age > 55:
        wants_photo = input("Do you want a photo taken? Type Y for yes or N for no. ")
        if wants_photo == 'Y':
            bill += 3
    
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")
```

### Explanation
1. **Height Check**: Ensure the user is tall enough to ride.
2. **Age Check**: 
   - Under 12: $5
   - 12 to 18: $7
   - 45 to 55: Free ride (prints a message and doesn't modify the bill)
   - Over 18 (but not 45 to 55): $12
3. **Photo Option**: 
   - Asked only if the user's age is not between 45 and 55.
   - Adds $3 to the bill if the user wants a photo.
4. **Output**: Final bill displayed with the calculated amount.

### Key Points
- **Logical Operators**: Allow for combining multiple conditions in one line.
- **`if`/`elif`/`else` Block**: Handles mutually exclusive conditions.
- **Independent Conditions**: Use separate `if` statements for additional checks.

## Practice 5 - Love Calculator

💪 This is a difficult challenge! 💪
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs.

Then check for the number of times the letters in the word LOVE occurs.

Then combine these numbers to make a 2 digit number.

For Love Scores **less than 10** or **greater than 90**, the message should be:

"Your score is *x*, you go together like coke and mentos."
For Love Scores **between 40 and 50**, the message should be:

"Your score is *y*, you are alright together."
Otherwise, the message will just be their score. e.g.:

"Your score is *z*."
e.g.

```
name1 = "Angela Yu"
name2 = "Jack Bauer"
```

T occurs 0 times

R occurs 1 time

U occurs 2 times

E occurs 2 times

Total = 5

L occurs 1 time

O occurs 0 times

V occurs 0 times

E occurs 2 times

Total = 3

Love Score = 53

Print: "Your score is 53."

**These functions will help you:**

[lower()](https://www.w3schools.com/python/ref_string_lower.asp) 

[count()](https://www.w3schools.com/python/ref_list_count.asp)

**Example Input 1**
```
Kanye West
Kim Kardashian
```
**Example Output 1**
```
The Love Calculator is calculating your score...
Your score is 42, you are alright together.
```
**Example Input 2**
```
Brad Pitt
Jennifer Aniston
```
**Example Output 2**
```
The Love Calculator is calculating your score...
Your score is 73.
```

**Hint**
You can test your values using this table:

|Name 1|Name 2|Score|
|---|---|---|
|Brad Pit|Jennifer Aniston	|73
|Prince William	|Kate Middleton	|67
|Ashton Kutcher	|Mila Kunis	|63
|Angela Yu	|Jack Bauer	|53
|David Beckham	|Victoria Beckham	|45
|Mario	|Princess Peach	|43
|Kanye West	|Kim Kardashian	|42


## Project 3 - Treasure Island / "Choose Your Own Adventure" Game

### Overview
Develop a simple interactive "Choose Your Own Adventure" game using Python. The game will prompt the player to make choices at various stages, leading to different outcomes based on their decisions. The project will utilize conditional statements (if, else, elif) and input handling to create a branching narrative.

### Objectives
1. **Implement User Choices**: Allow the player to make choices that affect the story's outcome.
2. **Use Conditional Logic**: Employ if, else, and elif statements to manage the flow of the game based on player decisions.
3. **Handle User Input Robustly**: Ensure the game correctly interprets user input regardless of capitalization.
4. **Create a Clear and Engaging Narrative**: Develop a storyline with multiple possible endings.



### Requirements
1. **Initial Setup**:
   - Start with an introductory message that sets the scene.
   - Ask the player if they want to go "left" or "right" at a crossroad.
   
2. **First Decision Point**:
   - If the player chooses "left", proceed to the next stage.
   - If the player chooses "right" or any other option, print a game-over message and end the game.
   
3. **Second Decision Point**:
   - For those who chose "left", ask whether they want to "wait for a boat" or "swim across" a lake.
   - If the player chooses "swim", print a game-over message indicating an attack by a creature and end the game.
   - If the player chooses "wait", proceed to the final decision point.
   
4. **Final Decision Point**:
   - Present three doors (red, yellow, blue) and ask the player to choose one.
   - If the player chooses "yellow", print a message indicating they have found the treasure and won the game.
   - If the player chooses "red" or "blue", print different game-over messages specific to each choice and end the game.
   - If the player chooses any other option, print a generic game-over message.

5. **Robust Input Handling**:
   - Ensure the game can handle inputs in any case (e.g., "LEFT", "left", "Left").
   
6. **Narrative and Creativity**:
   - Use your creativity to enhance the story, providing detailed descriptions and unique game-over reasons.

### Deliverables
1. **Python Script**: A fully functional Python script implementing the described game.
2. **Documentation**: Comments in the code explaining the logic and flow of the game.
3. **Flowchart**: A flowchart illustrating the decision points and possible outcomes in the game.

### Evaluation Criteria
1. **Functionality**: The game should run without errors and handle various inputs gracefully.
2. **Creativity**: The narrative should be engaging and imaginative.
3. **Code Quality**: The code should be well-organized and commented.
4. **User Experience**: The game should provide clear instructions and feedback to the player.

[Sample Flow Chart](https://viewer.diagrams.net/index.html?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload#%7B%22pageId%22%3A%22C5RBs43oDa-KdzZeNtuy%22%7D)

[ASCII art](https://ascii.co.uk/art)

[Demo](https://appbrewery.github.io/python-day3-demo/)