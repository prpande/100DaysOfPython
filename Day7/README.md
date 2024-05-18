# Day 7 - Hangman<!-- omit in toc -->

[Demo](https://appbrewery.github.io/python-day7-demo/)

Consolidation Project day for all the learnings so far.

- [Introduction to the Hangman Game](#introduction-to-the-hangman-game)
  - [Developing a Hangman Game: Flowchart Programming](#developing-a-hangman-game-flowchart-programming)
  - [Steps to Create a Flowchart](#steps-to-create-a-flowchart)
  - [Detailed Breakdown of Flowchart Logic](#detailed-breakdown-of-flowchart-logic)
  - [Implementing the Flowchart in Code](#implementing-the-flowchart-in-code)
  - [Tips for Development](#tips-for-development)
  - [Conclusion](#conclusion)
- [Step 1 - Picking a Random Word and Checking Answers](#step-1---picking-a-random-word-and-checking-answers)
  - [Getting Started](#getting-started)
  - [Task Overview](#task-overview)
  - [Additional Notes](#additional-notes)
- [Step 2 - Replacing Blanks with Guesses](#step-2---replacing-blanks-with-guesses)
  - [Getting Started](#getting-started-1)
  - [Task Overview](#task-overview-1)
  - [Additional Notes](#additional-notes-1)
- [Step 3 - Checking if the Player has Won](#step-3---checking-if-the-player-has-won)
  - [Objective](#objective)
  - [Task Overview](#task-overview-2)
  - [Detailed Steps](#detailed-steps)
  - [Additional Notes](#additional-notes-2)
- [Step 4 - Keeping Track of the Player's Lives](#step-4---keeping-track-of-the-players-lives)
  - [Objective](#objective-1)
  - [Task Overview](#task-overview-3)
  - [Detailed Steps](#detailed-steps-1)
  - [Additional Notes](#additional-notes-3)
  - [Next Steps](#next-steps)
- [Step 5 - Improving the User Experience](#step-5---improving-the-user-experience)
  - [Objective](#objective-2)
  - [Task Overview](#task-overview-4)
  - [Additional Notes](#additional-notes-4)




## Introduction to the Hangman Game

- **Objective**: To understand the game mechanics and translate them into a program.
- **Recommendation**:
  - Familiarize yourself with the game by playing it online or reading its Wikipedia page.
  - Understand that the game involves guessing letters to complete a word, with a limited number of incorrect guesses allowed.

### Developing a Hangman Game: Flowchart Programming
- **Purpose**: To visually map out the game logic before coding.
- **Task**: Create a flowchart to represent the steps and decisions in the game.

### Steps to Create a Flowchart
1. **Start the Game**:
   - Generate a random word (e.g., "mouse").
   - Display blank spaces equal to the number of letters in the word.
   
2. **User Guess**:
   - Prompt the user to guess a letter.
   - Check if the guessed letter is in the word.

3. **Correct Guess**:
   - If the letter is in the word:
     - Replace the corresponding blanks with the guessed letter.
     - Check if all blanks are filled.
     - If yes, the user wins the game.
     - If no, prompt for another guess.

4. **Incorrect Guess**:
   - If the letter is not in the word:
     - Deduct a life.
     - Draw a part of the hangman.
     - Check if the user has run out of lives.
     - If yes, the user loses the game.
     - If no, prompt for another guess.

### Detailed Breakdown of Flowchart Logic
- **Initial Setup**:
  - Generate a random word (e.g., "mouse").
  - Display blanks for each letter: `_ _ _ _ _`.
  
- **User Interaction**:
  - **Guessing a Letter**:
    - User guesses 'O':
      - Check if 'O' is in "mouse": Yes.
      - Replace blank with 'O': `_ O _ _ _`.
      - Check if all blanks are filled: No.
      - Continue to next guess.
      
    - User guesses 'Z':
      - Check if 'Z' is in "mouse": No.
      - Deduct a life and draw part of the hangman.
      - Check if all lives are lost: No.
      - Continue to next guess.
      
- **Winning the Game**:
  - If all letters are guessed correctly, the user wins.

- **Losing the Game**:
  - If all lives are lost, the user loses.

### Implementing the Flowchart in Code
- **Use Variables**:
  - `random_word`: The word to guess.
  - `blanks`: The current state of blanks and correctly guessed letters.
  - `lives`: The number of incorrect guesses allowed.

### Tips for Development
- **Flowchart Reference**: Keep the flowchart handy to guide the coding process.
- **Testing**: Test each part of the game logic separately to ensure accuracy.
- **Debugging**: Use print statements to check the flow of the program and the values of variables.

### Conclusion
- **Flowcharts**: Useful for planning and visualizing complex logic.
- **Programming**: Break down the problem into smaller steps and implement them sequentially.
- **Next Steps**: Start coding the hangman game by following the flowchart logic.

## Step 1 - Picking a Random Word and Checking Answers

- Begin coding the Hangman game by selecting a random word and checking if a user's guessed letter is in that word.

### Getting Started
1. **Access Starting File**:
   - Use the provided Repl.it file from the course resources.
   - The file will be mostly empty except for a list of three words: "aardvark," "baboon," and "camel."

### Task Overview
- **Step 1**: Choose a random word from the list.
  - Use the `random` module to select a word from the list.
- **Step 2**: Prompt the user to guess a letter.
- **Step 3**: Check if the guessed letter is in the chosen word and display the result.
  - Loop through each letter in the chosen word to check if it matches the user's guess.
  - Inform the user about the match.

### Additional Notes
- **Testing**:
  - Print the chosen word during development to verify the correctness of your logic.
  - Test the program with different guesses to ensure it correctly identifies matching and non-matching letters.

- **Debugging Tips**:
  - If your code isn't working as expected, insert print statements to check the values of variables and the flow of the program.
  - Ensure that user input is properly converted to lowercase to avoid case-sensitivity issues.

[Python List Documentation](https://developers.google.com/edu/python/lists#for-and-in)

## Step 2 - Replacing Blanks with Guesses

- Extend the Hangman game to create a list of underscores representing the letters in the chosen word. Update the list with the correct letters as the user guesses them correctly.

### Getting Started
1. **Access Starting File**:
   - Use the provided Repl.it file from the course resources.
   - The file will contain a list of words and a print statement to reveal the chosen word for debugging purposes.

### Task Overview
- **Step 1 Recap**: Select a random word and prompt the user for a letter guess.
- **Step 2 Tasks**:
  1. Generate a list of underscores, each representing a letter in the chosen word.
  2. Update the list with the correct letter if the user guesses correctly.
     - Loop through each letter in the chosen word.
     - If the guessed letter matches, update the corresponding position in the list.
  3. Print the list to show the current state of the word with correct guesses and underscores.

### Additional Notes
- **Testing**:
  - Use different words and guesses to verify the accuracy of your implementation.
  - Ensure the print statement helps you debug by showing the chosen word.

- **Debugging Tips**:
  - If your code isn't working as expected, check the loops and conditions.
  - Ensure that the guessed letter is properly compared and the list is updated accurately.

## Step 3 - Checking if the Player has Won

### Objective
- Enhance the Hangman game to repeatedly allow the user to guess letters until they either guess the word correctly or fail.

### Task Overview
1. Use a `while` loop to continually prompt the user to guess letters.
2. Update the display list with correct guesses.
3. Check if the word has been completely guessed to end the game.

### Detailed Steps

1. **While Loop for Repeated Guesses**:
   - Use a `while` loop to keep the game running until all blanks are filled.
   - The condition for the loop to continue is having underscores in the `display` list.

2. **Check for Completion**:
   - Inside the `while` loop, check if there are any underscores left in the `display` list.
   - If no underscores are left, the user has guessed the word correctly.

3. **Using the 'in' Keyword and Negation**:
   - The `in` keyword helps check if an underscore is still in the `display` list.
   - Use the `not` keyword to negate the condition for the loop to run until there are no underscores left.

### Additional Notes
- **Testing**:
  - Run the game multiple times, making both correct and incorrect guesses to ensure it works as expected.
  - Debugging: Use print statements to verify the chosen word and the state of the display list during the game.

- **Hints**:
  - **`while "_" in display`**: This condition keeps the loop running as long as there's at least one underscore in the `display` list.
  - **Negation with `not`**: For example, `while not "_" in display` is equivalent to `while "_" not in display`.

## Step 4 - Keeping Track of the Player's Lives

### Objective
- Enhance the Hangman game by incorporating ASCII art to visually represent the hangman stages and adding functionality to track and display remaining lives.

### Task Overview
1. Incorporate ASCII art to represent hangman stages.
2. Track the number of lives the player has.
3. Deduct a life for each incorrect guess.
4. End the game when lives run out and display a "You lose" message.
5. Print the corresponding ASCII art stage based on remaining lives.

### Detailed Steps

1. **Initialize Lives and ASCII Art**:
   - Create a variable `lives` initialized to 6.
   - Use a list of ASCII art strings to represent each stage of the hangman.

2. **Update Lives for Incorrect Guesses**:
   - Check if the guessed letter is not in the chosen word.
   - Decrease the `lives` by 1 for each incorrect guess.
   - Print the corresponding stage of ASCII art based on the number of remaining lives.

3. **Game End Conditions**:
   - The game ends if the `lives` reach 0 with a "You lose" message.
   - The game also ends if the user correctly guesses all the letters.

### Additional Notes
- **Testing**:
  - Run the game multiple times, making both correct and incorrect guesses to ensure it works as expected.
  - Debugging: Use print statements to verify the chosen word and the state of the display list during the game.

- **Hints**:
  - **ASCII Art**: The list `stages` contains the visual representation of the hangman. Each incorrect guess updates the stage.
  - **Lives Variable**: Track the number of incorrect guesses. When it reaches zero, the game ends.

### Next Steps
- After successfully implementing the ASCII art and lives functionality, the game now provides visual feedback on incorrect guesses.
- In future steps, you can add more features such as input validation, advanced word selection, or a more sophisticated user interface.

## Step 5 - Improving the User Experience

### Objective
- Finalize the Hangman game by improving user experience and functionality. Specifically, incorporate a larger word list, use ASCII art for game stages and logo, and provide user feedback on repeated or incorrect guesses.

### Task Overview 
1. **Expand the Word List**:
   - Replace the simple word list with a comprehensive list from `hangman_words.py`.

2. **Import Hangman Art and Logo**:
   - Use `hangman_art.py` to import ASCII art stages and the hangman logo.

3. **Provide Feedback for Repeated Guesses**:
   - Inform the user if they have already guessed a letter.

4. **Provide Feedback for Incorrect Guesses**:
   - Inform the user if the guessed letter is not in the word and reduce a life.

### Additional Notes
- **Testing**:
  - Ensure thorough testing by making correct and incorrect guesses to validate the game functionality.
  - Debugging: Use print statements to verify the correct word and the current state of the display list during the game.

- **Hints**:
  - **Modules and Imports**: Review how to import and use modules in Python. [Documentation](https://www.askpython.com/python/python-import-statement)
  - **Feedback Mechanisms**: Enhance user experience by providing clear feedback on their guesses.
