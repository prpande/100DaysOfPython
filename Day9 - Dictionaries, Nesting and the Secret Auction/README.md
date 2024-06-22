# Day 9 - Dictionaries, Nesting and the Secret Auction <!-- omit in toc -->

- [Lesson 20 - The Python Dictionary: Deep Dive](#lesson-20---the-python-dictionary-deep-dive)
  - [Overview](#overview)
  - [Key Concepts](#key-concepts)
  - [Common Pitfalls](#common-pitfalls)
  - [Practical Applications](#practical-applications)
  - [Example Code](#example-code)
- [Practice 1 - Grading Program](#practice-1---grading-program)
- [Lesson 21 - Nesting Lists and Dictionaries](#lesson-21---nesting-lists-and-dictionaries)
  - [Overview](#overview-1)
  - [Key Concepts](#key-concepts-1)
  - [Practical Examples](#practical-examples)
    - [Example 1: List in a Dictionary](#example-1-list-in-a-dictionary)
    - [Example 2: Dictionary in a Dictionary](#example-2-dictionary-in-a-dictionary)
    - [Example 3: Dictionary in a List](#example-3-dictionary-in-a-list)
  - [Nesting Examples Explained](#nesting-examples-explained)
  - [Benefits of Nesting](#benefits-of-nesting)
- [Practice 2 - Dictionary in List](#practice-2---dictionary-in-list)
- [Project 9 - The Secret Auction Program](#project-9---the-secret-auction-program)


## Lesson 20 - The Python Dictionary: Deep Dive

### Overview
Dictionaries in Python are similar to real-life dictionaries. They are collections that store data in key-value pairs, allowing for efficient data retrieval and organization.

### Key Concepts
1. **Definition and Structure**
   - A dictionary consists of keys and associated values.
   - Syntax: `{key1: value1, key2: value2, ...}`
   - Example: `{'bug': 'An error in a program that prevents the program from running as expected'}`

2. **Creating a Dictionary**
   - Use curly braces `{}` to define a dictionary.
   - Separate keys and values with a colon `:`.
   - Separate key-value pairs with commas `,`.
   - Example:
     ```python
     programming_dictionary = {
         'bug': 'An error in a program that prevents the program from running as expected',
         'function': 'A piece of code that you can easily call over and over again'
     }
     ```

3. **Formatting for Readability**
   - Start the dictionary with an opening curly brace `{`.
   - Indent each key-value pair.
   - Place a comma at the end of each entry, even the last one for ease of future additions.
   - Close the dictionary with a closing curly brace `}`.

4. **Accessing Values**
   - Use square brackets `[]` with the key to retrieve values.
   - Example:
     ```python
     print(programming_dictionary['bug'])
     # Output: 'An error in a program that prevents the program from running as expected'
     ```

5. **Adding and Updating Entries**
   - Add a new key-value pair using the assignment operator `=`.
   - Example:
     ```python
     programming_dictionary['loop'] = 'The action of doing something over and over again'
     ```
   - Update an existing key-value pair similarly.
   - Example:
     ```python
     programming_dictionary['bug'] = 'A moth in your computer'
     ```

6. **Deleting Entries**
   - Use the `del` keyword to remove a key-value pair.
   - Example:
     ```python
     del programming_dictionary['bug']
     ```

7. **Clearing a Dictionary**
   - Assign an empty dictionary `{}` to clear all entries.
   - Example:
     ```python
     programming_dictionary = {}
     ```

8. **Iterating Through a Dictionary**
   - Use a `for` loop to iterate through keys.
   - Example:
     ```python
     for key in programming_dictionary:
         print(key, programming_dictionary[key])
     ```

### Common Pitfalls
- **Key Errors**: Ensure keys are spelled correctly and are the correct data type.
- **Empty Dictionaries**: Start with an empty dictionary when you need to build it up later.
- **Data Types**: Keys must be immutable data types (e.g., strings, numbers, tuples).

### Practical Applications
- **Fetching Data**: Retrieve specific data points using their keys.
- **Data Management**: Store and manage related data efficiently.
- **Dynamic Updates**: Add, update, and delete entries as needed in your programs.

### Example Code
Here is a full example demonstrating various operations on a dictionary:
```python
# Creating a dictionary
programming_dictionary = {
    'bug': 'An error in a program that prevents the program from running as expected',
    'function': 'A piece of code that you can easily call over and over again'
}

# Accessing a value
print(programming_dictionary['bug'])

# Adding a new entry
programming_dictionary['loop'] = 'The action of doing something over and over again'

# Updating an existing entry
programming_dictionary['bug'] = 'A moth in your computer'

# Iterating through the dictionary
for key in programming_dictionary:
    print(key, programming_dictionary[key])

# Clearing the dictionary
programming_dictionary = {}
print(programming_dictionary)  # Output: {}
```
## Practice 1 - Grading Program

You have access to a database of `student_scores` in the format of a dictionary. The **keys** in `student_scores` are the names of the students and the values are their exam scores.

Write a program that **converts their scores to grades**. By the end of your program, you should have a new dictionary called `student_grades` that should contain student names for **keys** and their **grades** for **values**.

The **final version** of the `student_grades` dictionary will be checked.

**DO NOT** modify lines 1-7 to change the existing `student_scores` dictionary.

**DO NOT** write any print statements.

This is the scoring criteria:

- Scores 91 - 100: Grade = "Outstanding"
- Scores 81 - 90: Grade = "Exceeds Expectations"
- Scores 71 - 80: Grade = "Acceptable"
- Scores 70 or lower: Grade = "Fail"

**Expected Output**

```
'{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}'
```

**Hint**

- Remember that looping through a Dictionary will only give you the keys and not the values.
- If in doubt as to why your code is not doing what you expected, you can always print out the intermediate values.
- At the end of your program, the print statement will show the final student_scores dictionary, do not change this.

## Lesson 21 - Nesting Lists and Dictionaries

### Overview
Nesting in Python involves placing one collection type inside another. This can be a list inside a dictionary, a dictionary inside a list, or even more complex structures like dictionaries inside dictionaries. Nesting is useful for representing more complex data structures.

### Key Concepts
1. **Nesting Lists in Dictionaries**
   - A list can be a value in a dictionary.
   - Example:
     ```python
     travel_log = {
         "France": ["Paris", "Lille", "Dijon"],
         "Germany": ["Berlin", "Hamburg", "Stuttgart"]
     }
     ```
   - Here, the value for each country key is a list of cities.

2. **Nesting Dictionaries in Dictionaries**
   - A dictionary can be a value in another dictionary.
   - This allows for more detailed and complex data storage.
   - Example:
     ```python
     travel_log = {
         "France": {
             "cities_visited": ["Paris", "Lille", "Dijon"],
             "total_visits": 12
         },
         "Germany": {
             "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
             "total_visits": 5
         }
     }
     ```
   - Each country key has a dictionary as its value, storing both cities visited and the total number of visits.

3. **Nesting Dictionaries in Lists**
   - A list can contain dictionaries, allowing for an ordered collection of dictionaries.
   - Example:
     ```python
     travel_log = [
         {
             "country": "France",
             "cities_visited": ["Paris", "Lille", "Dijon"],
             "total_visits": 12
         },
         {
             "country": "Germany",
             "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
             "total_visits": 5
         }
     ]
     ```
   - Here, each element in the list is a dictionary containing details about each country.

### Practical Examples

#### Example 1: List in a Dictionary
```python
# Dictionary with list values
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}
```

#### Example 2: Dictionary in a Dictionary
```python
# Dictionary with dictionary values
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
}
```

#### Example 3: Dictionary in a List
```python
# List containing dictionaries
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
]
```

### Nesting Examples Explained

1. **Accessing Nested Data**
   - Accessing nested lists:
     ```python
     print(travel_log["France"][0])  # Output: Paris
     ```
   - Accessing nested dictionaries:
     ```python
     print(travel_log["France"]["cities_visited"])  # Output: ["Paris", "Lille", "Dijon"]
     ```
   - Accessing dictionaries in a list:
     ```python
     print(travel_log[0]["country"])  # Output: France
     ```

2. **Modifying Nested Data**
   - Adding a new city to the list of cities in France:
     ```python
     travel_log["France"]["cities_visited"].append("Nice")
     ```
   - Updating the total number of visits to Germany:
     ```python
     travel_log["Germany"]["total_visits"] = 6
     ```
   - Adding a new country entry in the list:
     ```python
     travel_log.append({
         "country": "Italy",
         "cities_visited": ["Rome", "Florence"],
         "total_visits": 2
     })
     ```

### Benefits of Nesting
- **Organization**: Keeps related data grouped together in a structured way.
- **Flexibility**: Allows storage of complex and detailed information.
- **Scalability**: Makes it easier to expand and modify data structures.

## Practice 2 - Dictionary in List

You are going to write a program that adds to a `travel_log`. You can see a `travel_log` which is a **List** that contains 2 **Dictionaries**. Your job is to create a function that can add new countries to this list.

Write a function that will work with the following line of code on line 21 to add the entry for Brazil to the `travel_log`.

```python
add_new_country("Brazil", 5, ["Sao Paulo", "Rio de Janeiro"])
```
**DO NOT** modify the `travel_log` directly. The goal is to create a function that modifies it.

**Example Input**
```
Brazil
5
["Sao Paulo", "Rio de Janeiro"]
```

**Example Output**
```
I've been to Brazil 5 times.
My favourite city was Sao Paulo.
```

**Hint**

- Look at the function call above to see what the name of the function should be.
- The inputs for the function are positional arguments. The order is very important.
- Feel free to choose your own parameter names.

## Project 9 - The Secret Auction Program

[Demo](https://appbrewery.github.io/python-day9-demo/)

**Objective:**
Develop a blind auction program that allows multiple users to place bids in a secure and private manner. The program will determine the highest bidder and announce the winner at the end of the auction.

**Requirements:**

1. **Display Initial Information:**
   - Show the program logo and a brief description of the auction process.

2. **User Input:**
   - Prompt each user for their name and bid amount.
   - After each bid, ask if there are any other bidders.

3. **Bid Privacy:**
   - Clear the screen after each bid to maintain privacy and prevent other users from seeing previous bids.

4. **Dictionary Storage:**
   - Store each bid in a dictionary with the user's name as the key and the bid amount as the value.

5. **Determine Highest Bid:**
   - Once all bids are entered, loop through the dictionary to find the highest bid.
   - Announce the winner and their bid amount.

**Detailed Steps:**

1. **Initialization:**
   - Import necessary modules, including a clear screen function.
   - Display the auction logo and introductory text.

2. **Bid Collection:**
   - Continuously prompt users for their name and bid amount.
   - Store each entry in a dictionary.
   - After each entry, ask if there are more bidders.
   - Use the clear screen function to maintain bid privacy.

3. **End of Bidding:**
   - When no more bidders are present, process the bids.
   - Iterate through the dictionary to find the highest bid.
   - Announce the winner and their bid amount.

**Additional Features:**
- Implement input validation to ensure bid amounts are valid numbers.
- Provide an option to restart the auction after a winner is declared.

**Assumptions:**
- The program runs in a console or terminal environment.
- The user is familiar with basic input methods.

This project aims to test and apply knowledge of Python dictionaries, user input handling, and basic control flow structures. By the end of this project, users will have a solid understanding of how to implement a blind auction using Python.