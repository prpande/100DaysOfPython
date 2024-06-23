# Project Virtual Coffee Machine
from art import logo
from os import system, name

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def clear():
    system('cls' if name == 'nt' else 'clear')


def generate_report():
    print(f"Water\t:\t{resources['water']}ml")
    print(f"Milk\t:\t{resources['milk']}ml")
    print(f"Coffee\t:\t{resources['coffee']}g")
    print(f"Money\t:\t${resources['money']}")


def check_resources(drink):
    ingredients = MENU[drink]["ingredients"]
    if resources["water"] < ingredients["water"]:
        print("Sorry there is not enough water.")
    elif "milk" in ingredients and resources["milk"] < ingredients["milk"]:
        print("Sorry there is not enough milk.")
    elif resources["coffee"] < ingredients["coffee"]:
        print("Sorry there is not enough coffee.")
    else:
        return True
    return False


def display_menu():
    print()
    return input("What would you like? (espresso/latte/cappuccino): ").lower()


def dispense_drink(drink):
    ingredients = MENU[drink]["ingredients"]
    resources["water"] -= ingredients["water"]
    if "milk" in ingredients:
        resources["milk"] -= ingredients["milk"]
    resources["coffee"] -= ingredients["coffee"]
    resources["money"] += MENU[drink]["cost"]
    print(f"\nHere is your {drink} ☕. Enjoy!")


def collect_money(drink):
    print("Please insert coins.")
    # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    total_money = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    drink_cost = MENU[drink]["cost"]
    print()
    if total_money < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        if total_money > drink_cost:
            print(f"Here is ${round(total_money-drink_cost, 2)} dollars in change.")
        return True


def run_machine():
    while True:
        print(logo)
        choice = display_menu()
        print()
        if choice == "report":
            generate_report()
        elif choice == "off":
            return
        elif check_resources(choice) and collect_money(choice):
            dispense_drink(choice)


clear()
run_machine()
