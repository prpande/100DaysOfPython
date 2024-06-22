# Day 13 - Debugging: How to Find and Fix Errors in your Code<!-- omit in toc -->

- [Introduction to Debugging](#introduction-to-debugging)
- [Historical Context](#historical-context)
- [Approach to Debugging](#approach-to-debugging)
- [Steps and Techniques in Debugging](#steps-and-techniques-in-debugging)
  - [Step 1: Describe the Problem](#step-1-describe-the-problem)
  - [Example Walkthrough](#example-walkthrough)
    - [Initial Setup](#initial-setup)
    - [Example Debugging Problem](#example-debugging-problem)
    - [Description of the Problem](#description-of-the-problem)
  - [Step 2: Test Assumptions](#step-2-test-assumptions)
  - [Step 3: Implement the Fix](#step-3-implement-the-fix)
    - [Verification](#verification)
  - [Conclusion](#conclusion)
- [Reproducing Bugs](#reproducing-bugs)
  - [Step-by-Step Guide](#step-by-step-guide)
    - [Step 1: Isolate the Bug](#step-1-isolate-the-bug)
    - [Step 2: Run the Code](#step-2-run-the-code)
    - [Step 3: Reproduce the Error](#step-3-reproduce-the-error)
  - [Example Walkthrough](#example-walkthrough-1)
    - [Initial Analysis](#initial-analysis)
    - [Identifying the Issue](#identifying-the-issue)
    - [Reproducing the Bug](#reproducing-the-bug)
  - [Step 4: Fix the Code](#step-4-fix-the-code)
  - [Verification](#verification-1)
  - [Conclusion](#conclusion-1)
- [Playing Computer](#playing-computer)
  - [Step-by-Step Guide](#step-by-step-guide-1)
    - [Step 1: Isolate the New Block](#step-1-isolate-the-new-block)
    - [Step 2: Analyze the Code](#step-2-analyze-the-code)
  - [Example Walkthrough](#example-walkthrough-2)
    - [Initial Setup](#initial-setup-1)
    - [Reproducing the Bug](#reproducing-the-bug-1)
  - [Step 3: Playing Computer](#step-3-playing-computer)
    - [Step 4: Identify the Problem](#step-4-identify-the-problem)
  - [Step 5: Fix the Code](#step-5-fix-the-code)
  - [Verification](#verification-2)
  - [Conclusion](#conclusion-2)
- [Fixing Errors from the Editor](#fixing-errors-from-the-editor)
  - [Step-by-Step Guide](#step-by-step-guide-2)
    - [Step 1: Identify the Error](#step-1-identify-the-error)
    - [Step 2: Correct the Error](#step-2-correct-the-error)
- [Fixing Errors from the Console](#fixing-errors-from-the-console)
  - [Step-by-Step Guide](#step-by-step-guide-3)
    - [Step 1: Run the Code](#step-1-run-the-code)
    - [Step 2: Analyze the Console Error](#step-2-analyze-the-console-error)
    - [Step 3: Research the Error](#step-3-research-the-error)
    - [Step 4: Apply the Solution](#step-4-apply-the-solution)
    - [Step 5: Verify the Fix](#step-5-verify-the-fix)
  - [Example Walkthrough](#example-walkthrough-3)
    - [Initial Error](#initial-error)
    - [Corrected Code](#corrected-code)
- [Dealing with Logical Errors](#dealing-with-logical-errors)
  - [Step-by-Step Guide](#step-by-step-guide-4)
    - [Step 1: Identify the Issue](#step-1-identify-the-issue)
    - [Step 2: Apply the Fix](#step-2-apply-the-fix)
  - [Developing Debugging Skills](#developing-debugging-skills)
  - [Conclusion](#conclusion-3)
- [Using Print Statements for Debugging](#using-print-statements-for-debugging)
  - [Step-by-Step Guide](#step-by-step-guide-5)
    - [Step 1: Isolate the New Block](#step-1-isolate-the-new-block-1)
    - [Step 2: Analyze the Code](#step-2-analyze-the-code-1)
  - [Example Walkthrough](#example-walkthrough-4)
    - [Initial Code](#initial-code)
    - [Reproducing the Bug](#reproducing-the-bug-2)
  - [Step 3: Using Print Statements](#step-3-using-print-statements)
    - [Adding Print Statements](#adding-print-statements)
    - [Observing the Output](#observing-the-output)
  - [Step 4: Identifying the Problem](#step-4-identifying-the-problem)
    - [Correcting the Code](#correcting-the-code)
  - [Step 5: Verify the Fix](#step-5-verify-the-fix-1)
  - [Key Takeaways](#key-takeaways)
- [Introduction to Debugging Tools](#introduction-to-debugging-tools)
  - [Print Statements for Debugging](#print-statements-for-debugging)
  - [Example: Using Print Statements](#example-using-print-statements)
  - [Corrected Code](#corrected-code-1)
- [Introduction to Debuggers](#introduction-to-debuggers)
  - [What is a Debugger?](#what-is-a-debugger)
  - [Using Python Tutor for Debugging](#using-python-tutor-for-debugging)
  - [Debugging Steps](#debugging-steps)
  - [Using Breakpoints](#using-breakpoints)
  - [Correcting the Code](#correcting-the-code-1)
  - [Benefits of Using a Debugger](#benefits-of-using-a-debugger)
- [Final Tips for Effective Debugging](#final-tips-for-effective-debugging)
  - [1. Take a Break](#1-take-a-break)
  - [2. Ask for Help](#2-ask-for-help)
  - [3. Run Code Frequently](#3-run-code-frequently)
  - [4. Tackle Bugs One at a Time](#4-tackle-bugs-one-at-a-time)
  - [5. Use Stack Overflow Wisely](#5-use-stack-overflow-wisely)
- [The Journey of Debugging](#the-journey-of-debugging)
- [Summary of Top 10 Debugging Tips](#summary-of-top-10-debugging-tips)



## Introduction to Debugging
- **Definition**: Debugging is the process of identifying and removing bugs or errors in code.
- **Common Experience**: As you write more code, encountering bugs is inevitable. It's a common part of the coding process.

## Historical Context
- **First Documented Bug**: 
  - **Pioneer**: Grace Hopper
  - **Incident**: Found a moth causing issues in a relay, marking the first recorded computer bug.

## Approach to Debugging
- **Mindset**: 
  - Creating bugs is a normal part of programming.
  - Instead of feeling discouraged, focus on identifying and resolving these bugs.

## Steps and Techniques in Debugging

### Step 1: Describe the Problem
- **Importance**: Understanding the problem is crucial to solving it.
- **Technique**: Clearly articulate what the code is supposed to do and identify where it fails.

### Example Walkthrough

#### Initial Setup
- **Starting Point**: Fork the starting repository for the day's code.
- **Process**: Uncomment blocks of code one by one to address debugging issues.

#### Example Debugging Problem
- **Scenario**: A function is supposed to print "You got it" when a loop reaches 20, but nothing gets printed.
- **Problem Identification**:
  - Analyze the function and its for-loop.
  - Determine the expected output and the actual behavior.

#### Description of the Problem
- **Code Analysis**:
  - The function loops through numbers 1 to 20.
  - It should print "You got it" when the loop counter (`i`) reaches 20.
- **Issue**: The print statement is not executed when `i` is expected to be 20.

### Step 2: Test Assumptions
- **Assumption**: The loop counter `i` will reach 20.
- **Reality**: The `range` function in Python excludes the stop value.
  - Example: `range(1, 20)` produces numbers from 1 to 19, not including 20.

### Step 3: Implement the Fix
- **Solution**: Adjust the range to ensure `i` reaches 20.
  - Change `range(1, 20)` to `range(1, 21)`.

#### Verification
- **Testing**: Run the modified code.
  - Expected Result: The function now prints "You got it" when the loop counter reaches 20.

### Conclusion
- **Key Takeaways**:
  - Always describe the problem thoroughly to understand the issue.
  - Test assumptions about the code's behavior and identify any false assumptions.
  - Apply the necessary fixes and verify the solution by testing.

## Reproducing Bugs
- **Importance**: Consistently reproducing a bug is crucial for effectively debugging it. If a bug appears intermittently, it becomes challenging to identify and fix.

### Step-by-Step Guide

#### Step 1: Isolate the Bug
- **Procedure**: 
  - Uncomment the new block of code.
  - Comment out the previous section to avoid confusion.

#### Step 2: Run the Code
- **Observation**: Sometimes the code works and prints a dice image from a list, but occasionally an error occurs.
- **Challenge**: Bugs that appear sporadically are difficult to diagnose since initial tests might not reveal the problem.

#### Step 3: Reproduce the Error
- **Goal**: Identify the conditions under which the error occurs.
- **Task**: Modify the code to consistently produce the error, making it easier to analyze.

### Example Walkthrough

#### Initial Analysis
- **Setup**: A list of dice images (emojis) and a random number (`dice_num`) generated between 1 and 6.
- **Error**: Sometimes an "index out of range" error occurs when trying to pick an item from the list using `dice_num`.

#### Identifying the Issue
- **Random Number Generation**: The `randint` function returns a random integer between the specified range, including both endpoints.
- **List Indexing**: Lists in Python are zero-indexed, meaning they start counting from 0.

#### Reproducing the Bug
- **Debugging Process**:
  - Print `dice_num` values to determine which one causes the error.
  - Observed that `dice_num = 6` causes the "index out of range" error.
  - Reason: The list has indices 0 to 5, but `dice_num` can be 6, which is outside this range.

### Step 4: Fix the Code
- **Solution**: Adjust the range of the random number generation to match the list indices.
  - Change `randint(1, 6)` to `randint(0, 5)`.

### Verification
- **Testing**: Run the modified code multiple times to ensure the error no longer occurs.
- **Result**: The code should work correctly without producing any "index out of range" errors, regardless of how many times it is executed.

### Conclusion
- **Key Takeaways**:
  - Reproducing a bug consistently is vital for understanding and fixing it.
  - Align random number generation ranges with list indices to prevent out-of-range errors.
  - Always verify the fix by testing the code multiple times.

## Playing Computer
- **Concept**: Pretend to be a computer and manually trace through the code to understand its execution.
- **Purpose**: Helps in identifying logical errors and understanding code flow, especially useful for debugging.

### Step-by-Step Guide

#### Step 1: Isolate the New Block
- **Procedure**: 
  - Comment out the previous block of code.
  - Uncomment the new block for analysis.

#### Step 2: Analyze the Code
- **Code Functionality**:
  - **Input**: Takes an integer input representing the user's year of birth.
  - **Condition Check**: Uses `if` statements to classify the user as a Millennial or Gen Z based on their birth year.

### Example Walkthrough

#### Initial Setup
- **Code Logic**:
  - If the year of birth is between 1980 and 1994 (inclusive), the user is classified as a Millennial.
  - If the year of birth is greater than 1994, the user is classified as Gen Z.

#### Reproducing the Bug
- **Scenario**: Input the year 1994 and observe the output.
- **Observation**: Nothing is printed when 1994 is entered, indicating a bug.

### Step 3: Playing Computer
- **Manual Trace**:
  - **Input**: 1994
  - **Check `if` Statement**: 
    - `if 1980 < year < 1994`: 
      - 1994 is greater than 1980 (True)
      - 1994 is not less than 1994 (False)
      - Result: False (True AND False = False)
  - **Next Condition**:
    - `elif year > 1994`: 
      - 1994 is not greater than 1994 (False)
      - Result: False

#### Step 4: Identify the Problem
- **Issue**: The conditions do not account for the year 1994, resulting in no classification being printed.

### Step 5: Fix the Code
- **Solution**: Adjust the conditions to include the year 1994.
  - Change `if 1980 < year < 1994` to `if 1980 < year <= 1994`
  - Alternatively, change `elif year > 1994` to `elif year >= 1994`

### Verification
- **Testing**: Run the code with the year 1994.
- **Expected Output**: The code should now print that the user is a Millennial or Gen Z, depending on the fixed condition.

### Conclusion
- **Key Takeaways**:
  - "Playing computer" helps in understanding and identifying logical errors in the code.
  - Ensure all possible input values are accounted for in conditional statements.
  - Always verify fixes by testing the code with various inputs.

## Fixing Errors from the Editor
- **Tip**: Always fix errors highlighted by the editor before continuing with coding.
- **Editor Errors**: The editor provides clues and highlights the line causing the error.
  - **Example**: An indented block expected error in a `print` statement.
  - **Solution**: Indent the block correctly to resolve the error.

### Step-by-Step Guide

#### Step 1: Identify the Error
- **Procedure**: Hover over the highlighted error in the editor to read the error message.
- **Example**: "Expected an indented block" error in a `print` statement.

#### Step 2: Correct the Error
- **Action**: Indent the block of code properly.
- **Result**: The error in the editor should disappear.

## Fixing Errors from the Console
- **Type of Errors**: These errors occur during code execution based on input or runtime conditions.
  - **Example**: An error occurs when a specific input is provided to the `age` variable.

### Step-by-Step Guide

#### Step 1: Run the Code
- **Scenario**: Run the code with different inputs to trigger the error.
- **Example**: Input "12" for age and observe the error in the console.

#### Step 2: Analyze the Console Error
- **Procedure**: Read the error message in the console to understand the issue.
- **Example**: Error due to attempting a numerical comparison with a string.

#### Step 3: Research the Error
- **Action**: Select non-specific parts of the error message (e.g., common terms) and search online.
- **Example**: Copy and paste relevant parts of the error message into Google.

#### Step 4: Apply the Solution
- **Finding**: Input from the console is a string and needs to be converted to an integer for numerical operations.
- **Solution**: Cast the input as an integer using `int()`.

#### Step 5: Verify the Fix
- **Action**: Run the corrected code with various inputs.
- **Result**: The code should no longer produce the error and should work as expected.

### Example Walkthrough

#### Initial Error
- **Code Snippet**:
  ```python
  age = input("Enter your age: ")
  if age > 18:
      print("You are an adult.")
  ```
- **Error**: Input is treated as a string, causing a comparison error.

#### Corrected Code
- **Solution**:
  ```python
  age = int(input("Enter your age: "))
  if age > 18:
      print("You are an adult.")
  ```
- **Verification**: Run the code and input different ages to ensure proper functionality.

## Dealing with Logical Errors
- **Type of Errors**: Code runs without syntax or runtime errors but does not produce the desired output.
  - **Example**: Incorrect string formatting causing unexpected output.

### Step-by-Step Guide

#### Step 1: Identify the Issue
- **Procedure**: Manually trace the code and understand the logic.
- **Example**: Missing f-string for variable insertion in a `print` statement.

#### Step 2: Apply the Fix
- **Solution**: Use an f-string to properly format the output.
  - **Code Snippet**:
    ```python
    name = "John"
    print(f"Hello, {name}!")
    ```
- **Verification**: Ensure the code produces the desired output with correct formatting.

### Developing Debugging Skills
- **Practice**: The more bugs you solve, the better you get at debugging.
- **Resources**: Use platforms like Stack Overflow and course-specific forums to help others and improve your skills.
- **Experience**: Each bug you solve enhances your debugging capabilities and builds experience.

### Conclusion
- **Key Takeaways**:
  - Fix errors highlighted by the editor promptly.
  - Analyze and research console errors to find solutions.
  - Manually trace and understand the logic for resolving logical errors.
  - Continuous practice and helping others strengthen your debugging skills.

## Using Print Statements for Debugging
- **Concept**: `print` is a valuable tool for debugging code by displaying the values of variables and the flow of execution.
- **Advantage**: Helps in understanding what the code is doing at specific points and identifying where things go wrong.

### Step-by-Step Guide

#### Step 1: Isolate the New Block
- **Procedure**: Comment out the previous block of code and uncomment the new block for analysis.

#### Step 2: Analyze the Code
- **Code Functionality**:
  - The program calculates the total number of words in a book based on user input for the number of pages and words per page.
  - **Variables**:
    - `pages` (initially 0)
    - `words_per_page` (initially 0)

### Example Walkthrough

#### Initial Code
- **Code Snippet**:
  ```python
  pages = 0
  words_per_page = 0
  
  pages = int(input("Enter the number of pages in your book: "))
  words_per_page = int(input("Enter the number of words per page: "))
  
  total_words = pages * words_per_page
  print(total_words)
  ```

#### Reproducing the Bug
- **Scenario**: Input 45 for pages and 250 for words per page.
- **Output**: 0, which is incorrect.

### Step 3: Using Print Statements
- **Action**: Insert `print` statements to display the values of `pages` and `words_per_page`.

#### Adding Print Statements
- **Code Snippet**:
  ```python
  pages = 0
  words_per_page = 0
  
  pages = int(input("Enter the number of pages in your book: "))
  words_per_page = int(input("Enter the number of words per page: "))
  
  print(f"Pages: {pages}")
  print(f"Words per page: {words_per_page}")
  
  total_words = pages * words_per_page
  print(total_words)
  ```

#### Observing the Output
- **Input**: 45 for pages and 250 for words per page.
- **Print Output**:
  ```
  Pages: 45
  Words per page: 0
  ```
- **Observation**: `words_per_page` is incorrectly set to 0.

### Step 4: Identifying the Problem
- **Issue**: The `words_per_page` variable is not capturing the correct user input due to a logical error.
- **Error**: The comparison operator `==` is mistakenly used instead of the assignment operator `=`.

#### Correcting the Code
- **Solution**: Replace `==` with `=` for the `words_per_page` assignment.
  - **Corrected Code Snippet**:
    ```python
    pages = 0
    words_per_page = 0
    
    pages = int(input("Enter the number of pages in your book: "))
    words_per_page = int(input("Enter the number of words per page: "))
    
    print(f"Pages: {pages}")
    print(f"Words per page: {words_per_page}")
    
    total_words = pages * words_per_page
    print(total_words)
    ```

### Step 5: Verify the Fix
- **Action**: Run the corrected code and input the same values.
- **Expected Output**: Correct total number of words calculated and printed.

### Key Takeaways
- **Using Print for Debugging**:
  - Print statements help trace the values of variables and understand the code flow.
  - Identify and isolate the exact location of the issue.
- **Common Mistakes**:
  - Misusing comparison `==` instead of assignment `=`.
- **Debugging Practice**:
  - Regularly using print statements can significantly aid in developing debugging skills.
  - Review and understand error messages to identify potential issues.

## Introduction to Debugging Tools

### Print Statements for Debugging
- **Importance**: Print statements are essential tools for debugging. They help track variable values and the flow of execution.
- **Usage**: 
  - Insert `print` statements to display the values of variables at specific points.
  - Useful for identifying where the code deviates from expected behavior.

### Example: Using Print Statements
- **Problem Statement**: Calculate the total number of words in a book.
- **Initial Code**:
  ```python
  pages = 0
  words_per_page = 0
  
  pages = int(input("Enter the number of pages in your book: "))
  words_per_page = int(input("Enter the number of words per page: "))
  
  total_words = pages * words_per_page
  print(total_words)
  ```
- **Issue**: The code outputs `0` instead of the expected total number of words.
- **Debugging with Print Statements**:
  ```python
  pages = 0
  words_per_page = 0
  
  pages = int(input("Enter the number of pages in your book: "))
  words_per_page = int(input("Enter the number of words per page: "))
  
  print(f"Pages: {pages}")
  print(f"Words per page: {words_per_page}")
  
  total_words = pages * words_per_page
  print(total_words)
  ```
- **Observation**: The `words_per_page` variable was not capturing the correct input due to a logical error.
- **Correction**: Replace the comparison operator `==` with the assignment operator `=`.

### Corrected Code
```python
pages = 0
words_per_page = 0

pages = int(input("Enter the number of pages in your book: "))
words_per_page = int(input("Enter the number of words per page: "))

print(f"Pages: {pages}")
print(f"Words per page: {words_per_page}")

total_words = pages * words_per_page
print(total_words)
```
- **Expected Output**: Correct total number of words calculated and printed.

## Introduction to Debuggers

### What is a Debugger?
- **Concept**: A debugger is a sophisticated tool that allows you to step through code, inspect variables, and control execution flow.
- **Advantages**:
  - Provides a detailed view of what the code is doing at each step.
  - Helps in identifying and resolving complex bugs.

### Using Python Tutor for Debugging
- **Example**: Debugging a function that mutates a list by multiplying each element by 2.
- **Initial Code**:
  ```python
  def mutate(a_list):
      b_list = []
      for item in a_list:
          new_item = item * 2
      b_list.append(new_item)
      print(b_list)
      
  mutate([1, 2, 3, 5, 8, 13])
  ```
- **Issue**: The code outputs `[26]` instead of a list with each element multiplied by 2.

### Debugging Steps
- **Step 1**: Copy the code into [Python Tutor](http://pythontutor.com).
- **Step 2**: Visualize execution to step through the code.
- **Step 3**: Observe variable values and control flow.
  - **Observation**: `b_list` only contains one value, `26`, due to the append operation being outside the loop.

### Using Breakpoints
- **Concept**: A breakpoint stops code execution at a specific line, allowing examination of variable values at that point.
- **Procedure**:
  - Set a breakpoint at the line where the issue is suspected.
  - Step through the code to observe the values of variables at each step.

### Correcting the Code
- **Problem**: `b_list.append(new_item)` is outside the loop.
- **Solution**: Move the append operation inside the loop.
  - **Corrected Code**:
    ```python
    def mutate(a_list):
        b_list = []
        for item in a_list:
            new_item = item * 2
            b_list.append(new_item)
        print(b_list)
    
    mutate([1, 2, 3, 5, 8, 13])
    ```
- **Expected Output**: `[2, 4, 6, 10, 16, 26]`

### Benefits of Using a Debugger
- **Enhanced Debugging**:
  - Automatically inspects all variables and their values.
  - Steps through code line by line.
  - Identifies the exact point where the code deviates from expected behavior.
- **Skill Development**:
  - Encourages a deeper understanding of code execution.
  - Builds proficiency in identifying and fixing bugs.

## Final Tips for Effective Debugging

### 1. Take a Break
- **Importance**: When stuck on a bug, stepping away from your code can provide a fresh perspective.
- **Practice**: 
  - Take short breaks or naps.
  - Return to the code with a clear mind.
- **Benefit**: Often, the solution becomes apparent after some downtime.

### 2. Ask for Help
- **Importance**: Getting another person's perspective can uncover assumptions you might have overlooked.
- **Sources**:
  - Fellow students or colleagues.
  - Online communities like Discord.
- **Benefit**: Fresh eyes can often spot the problem quickly.

### 3. Run Code Frequently
- **Importance**: Regularly testing small changes helps catch bugs early.
- **Practice**: 
  - Execute the code after small modifications.
  - Ensure each change works as expected before proceeding.
- **Benefit**: Prevents accumulating multiple bugs, making them easier to manage and fix.

### 4. Tackle Bugs One at a Time
- **Importance**: Focusing on individual bugs simplifies the debugging process.
- **Practice**:
  - Address each issue sequentially.
  - Avoid attempting to fix multiple bugs simultaneously.
- **Benefit**: Streamlines the debugging process, making it more manageable.

### 5. Use Stack Overflow Wisely
- **Importance**: A valuable resource for solving unique or complex bugs.
- **Practice**:
  - Search for similar issues before posting a new question.
  - Post questions only after exhausting other debugging avenues.
- **Benefit**: Efficiently utilizes community knowledge without over-relying on external help for simple issues.

## The Journey of Debugging

- **Expectation**: As you advance, bugs will become more complex.
- **Mindset**: Creating bugs is a natural part of programming and does not indicate failure.
- **Growth**: Debugging builds programming skills, akin to lifting weights at the gym—each bug fixed is a step towards becoming a better programmer.

## Summary of Top 10 Debugging Tips

1. **Take a Break**: Refresh your mind to gain new insights.
2. **Ask for Help**: Utilize the perspectives of others to identify issues.
3. **Run Code Often**: Test small changes frequently to catch bugs early.
4. **Tackle Bugs Individually**: Focus on one bug at a time for a streamlined process.
5. **Use Stack Overflow**: Leverage the community for unique or complex bugs.
6. **Stay Positive**: Bugs are a learning opportunity, not a sign of failure.
7. **Be Patient**: Debugging takes time and practice to master.
8. **Reflect on Progress**: Each bug fixed improves your programming skills.
9. **Collaborate**: Help others with their bugs to strengthen your own skills.
10. **Keep Learning**: Continually seek new strategies and tools for debugging.
