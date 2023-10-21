# Coffee Machine Program
# By Jazz
# Date 21/10/2023
# A simple coffee machine program with a reservoir of ingredients and recipes to make 3 differing drinks.

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
    "water": 3000,
    "milk": 2000,
    "coffee": 1000
}

money_in_machine = 0.00


def print_stock_report(dictn):
    """This is a simple function to print out the current stock report of the machine"""
    for item in dictn:
        print (item, ":" , dictn[item], "\n")


def drink_feasible(drink_selected, resources, drink_cost):
    """Need to pull in 2 dictionaries one is the choice the other is the resources and conclude if it can deliver drink"""
    # print(drink_selected["ingredients"]["water"])
    if "water" not in drink_selected["ingredients"] or drink_selected["ingredients"]["water"] <= resources["water"]:
        if "milk" not in drink_selected["ingredients"] or drink_selected["ingredients"]["milk"] <= resources["milk"]:
            if "coffee" not in drink_selected["ingredients"] or drink_selected["ingredients"]["coffee"] <= resources["coffee"]:
                customer_money = get_money()
                if customer_money >= drink_selected["cost"]:
                    resources["water"] -= drink_selected["ingredients"]["water"]
                    if "milk" in drink_selected["ingredients"]:
                        resources["milk"] -= drink_selected["ingredients"]["milk"]
                    resources["coffee"] -= drink_selected["ingredients"]["coffee"]
                    drink_cost += drink_selected["cost"]
                    change = customer_money - drink_cost
                    print(f"You drink is {drink_selected} costing {drink_cost} ")
                    print(f"Your change is ${change}")
            else:
                print("Not Enough Coffee")
                operational = False

        else:
            print("Not Enough Milk")
            operational = False
    else:
        print("Not Enough Water")
        operational = False


def get_money():
    quarters= int(input("How many quarters ?: ")) * 0.25
    dimes= int(input("How many dimes ?: ")) * 0.10
    nickels= int(input("How many nickels ?: ")) * 0.05
    pennies= int(input("How many pennies ?: ")) * 0.01
    customer_money = quarters + dimes + nickels + pennies
    return customer_money


def main_program():
    operational = True
    while operational:
        # TODO Print out the different drinks on offer
        drink_selection = input("What would you like? espresso, Latte, cappuccino: ")
        if drink_selection == "report":
            print_stock_report(resources)
        else:
            chosen_drink = MENU[drink_selection]
            drink_feasible(chosen_drink, resources, money_in_machine)
            print_stock_report(resources)


main_program()

