# Day 15 - Local Development Environment Setup & the Coffee Machine<!-- omit in toc -->

- [Importance of a Development Environment](#importance-of-a-development-environment)
- [Integrated Development Environment (IDE)](#integrated-development-environment-ide)
- [Popular IDEs for Python](#popular-ides-for-python)
- [Installing Python](#installing-python)
- [Downloading PyCharm](#downloading-pycharm)
- [Transition from Repl.it to PyCharm](#transition-from-replit-to-pycharm)
- [PyCharm Features](#pycharm-features)
- [Benefits of Using PyCharm](#benefits-of-using-pycharm)
- [Project Virtual Coffee Machine](#project-virtual-coffee-machine)
  - [Objective](#objective)
  - [Requirements](#requirements)
    - [Coffee Types and Recipes](#coffee-types-and-recipes)
    - [Initial Resources](#initial-resources)
    - [Coin Types and Values](#coin-types-and-values)
    - [Program Capabilities](#program-capabilities)
    - [Additional Features](#additional-features)
    - [User Interactions](#user-interactions)
    - [Program Specification](#program-specification)
    - [Project Setup](#project-setup)


## Importance of a Development Environment
- A proper development environment is crucial as projects become more complex.
- **Analogy**: Just as chefs need sharp knives, programmers need a good development environment.

## Integrated Development Environment (IDE)
- **Definition**: A software that helps in creating code by offering various tools.
- **Functions**:
  - Linting code
  - Finding errors
  - Providing coding style guidance
  - Debugging issues
- **Significance**: Transitions a developer from a newbie to a more skilled level.

## Popular IDEs for Python
- **Examples**: Jupyter, Spider, VS Code, Thonny
- **Chosen IDE for the Course**: PyCharm
  - **Description**: An Intelligent Development Environment specialized for Python
  - **Advantages**: Used by professionals, offers specialized tools for Python development

## Installing Python
1. **Accessing Python Download**:
   - [download link](https://www.python.org/downloads/)
   - The website will automatically detect the operating system.

2. **Installation on Windows**:
   - Download the latest version of Python.
   - Open the downloaded .exe file.
   - Ensure "Add Python 3.8 to Path" is checked.
   - Click "Install now".
   - Administrative privileges are required.
   - Follow prompts and allow permissions.
   - If prompted, disable path length limit.

3. **Installation on Mac**:
   - Download the latest version of Python from the course resources.
   - Follow the wizard: click continue, agree to terms, and install.
   - Administrative privileges are required.
   - Confirm installation by checking the folder for Python 3.8 or later versions.

## Downloading PyCharm
1. **Accessing PyCharm Download**:
   - [download link](https://www.jetbrains.com/pycharm/download/?section=windows)
   - Click on the Download button on the PyCharm homepage.

2. **Selecting the Correct Version**:
   - The webpage should automatically detect your operating system.
   - **For Windows Users**:
     - Confirm system compatibility by checking system requirements.
     - Follow simple installation instructions: Download and Run.
   - **For Mac Users**:
     - The process is virtually identical to Windows.
   - **For Linux Users**:
     - Toggle to the Linux tab.
     - Check system requirements and follow installation instructions.

3. **Choosing the Version**:
   - **Community Version**:
     - Free and open source.
     - Sufficient for all course needs.
   - **Professional Version**:
     - Offers a free trial.
     - Requires payment after the trial period.

4. **Downloading Process**:
   - Click on the Download button for the Community Edition.
   - Download time: Approximately 5 to 10 minutes.

## Transition from Repl.it to PyCharm
- **Previous Tool**: Repl.it
  - **Advantages**:
    - Easy to share code
    - Easy to fork code copies
  - **Limitations**:
    - Not suitable for advanced, complex projects
- **New Tool**: PyCharm
  - **Professional tool used by Python developers**

## PyCharm Features
1. **Spellcheck for English Words**:
   - Ensures correct spelling in variable names, keys, values, and print statements.
   - Helps avoid errors due to typos, especially in sensitive elements like dictionaries.
   - Example: Identifies "phon" as a typo and suggests "phone".

2. **Split-Screen Development**:
   - Allows viewing multiple files side by side.
   - Facilitates referencing other pieces of code while coding.
   - Example: Viewing contacts in a data file while writing code that accesses those contacts.

3. **Built-In Linter**:
   - Ensures code adheres to the PEP 8 style guide.
   - Provides guidance on spacing, line length, and other conventions.
   - Example: Highlights missing whitespace after a comma or incorrect number of blank lines around functions.

4. **Local History**:
   - Tracks and displays coding history.
   - Allows reverting to previous versions of the code.
   - Example: Viewing and restoring code from different time points within the last 12 hours.

5. **Code Structure Pane**:
   - Displays variables and functions in the code.
   - Facilitates quick navigation to specific code elements.
   - Example: Clicking on a function name in the structure pane to jump to its definition.

6. **Refactor and Rename**:
   - Allows renaming variables or functions across the entire codebase.
   - Ensures consistency and correctness without manual changes.
   - Example: Renaming "my_function" to "add" and updating all instances automatically.

## Benefits of Using PyCharm
- Enhanced productivity with professional-grade tools.
- Better code management and error prevention.
- Easier adherence to coding standards.
- More efficient development workflow.

## Project Virtual Coffee Machine

### Objective
To develop a virtual coffee machine program that mimics the functionality of a real-life coffee machine, capable of serving three types of coffee: espresso, latte, and cappuccino. The program will manage resources, process coin-operated transactions, and ensure accurate and consistent operations based on user inputs.

### Requirements

#### Coffee Types and Recipes
1. **Coffee Types**:
   - Espresso
   - Latte
   - Cappuccino

2. **Recipes**:
   - Each coffee type requires specific amounts of water, coffee, and milk.
   - Each coffee type has a distinct price.

#### Initial Resources
- **Water**: 300ml
- **Milk**: 200ml
- **Coffee**: 100g

#### Coin Types and Values
- **Penny**: 0.01 USD
- **Nickel**: 0.05 USD
- **Dime**: 0.10 USD
- **Quarter**: 0.25 USD

#### Program Capabilities
1. **Print Report**:
   - Display current resource levels (water, milk, coffee).
   - Show the amount of money accumulated.

2. **Check Resource Sufficiency**:
   - Ensure there are enough resources to make the selected drink.
   - Provide feedback if resources are insufficient.

3. **Process Coins**:
   - Accept coin input from the user.
   - Calculate the total monetary value of the inserted coins.
   - Ensure sufficient funds for the selected drink.
   - Provide change if necessary.
   - Refund coins if the amount is insufficient.

4. **Make Coffee**:
   - Deduct the required resources from the machine.
   - Add the cost of the drink to the machine's total money.

5. **Handle Transactions**:
   - Verify successful transactions.
   - Ensure correct operation without fraudulent inputs.

#### Additional Features
1. **Resource Deduction**:
   - Accurately subtract the required amounts of water, milk, and coffee for each drink.
   - Update the resource report accordingly.

2. **Error Handling**:
   - Inform the user if any resource is insufficient for the requested drink.
   - Refund the user's coins if the transaction fails.

#### User Interactions
1. **Prompt User Actions**:
   - Select a drink.
   - Insert coins.
   - Request a resource report.

2. **Output Feedback**:
   - Display transaction results.
   - Show updated resource levels after each transaction.

#### Program Specification
- Detailed specifications and requirements are provided in a downloadable PDF in the course resources.
- The final working version of the code is available for reference.

#### Project Setup
1. **Initial Code**:
   - Provided starting code in `main.py`.
   - Set up a new project in PyCharm named `coffee_machine`.
   - Create and use a `main.py` file for development.

2. **To-Do Tracking**:
   - Utilize PyCharm's to-do tracking feature to manage tasks.
   - Break down the problem into smaller, manageable to-dos.