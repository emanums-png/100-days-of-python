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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            return False
    return True

def process_coins():
    print("Insert your coins")
    total = int(input("How many euros")) * 1
    total += int(input("how many cents")) * 0.5
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f"Here is {change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy! ☕")




is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water {resources['water']}ml")
        print(f"Milk {resources['milk']}ml")
        print(f"Coffee {resources['coffee']}ml")
        print(f"Money €{profit}")
    else:
        order_drink = MENU[choice]
        order_ingredients = order_drink["ingredients"]
        can_make = is_resource_sufficient(order_ingredients)
        if can_make:
            money_received = process_coins()
            drink_cost = order_drink["cost"]
            if is_transaction_successful(money_received, drink_cost):
                make_coffee(choice, order_ingredients)


        else:
            print("Sorry, not enough resources to make.")





