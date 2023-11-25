from resorce import *


def print_report(money):
    """Prints the amount of milk coffee and water in the coffee machine no need to pass anything"""
    for key in resources.keys():
        print(f"{key} : {resources[key]}")
    print (f"Money : ${money}")


def money_process():
    # drink_cost = MENU[user_coffee_choice]['cost']
    print("Please insert coins.")
    quarters = int(input("How many Quarters? : "))
    dimes = int(input("How many Dimes? : "))
    nickles = int(input("How many Nickel? : "))
    pennies = int(input("How many Pennies? : "))
    total_money = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return total_money


def check_transaction_success(user_drink_choice, MENU, resources):
    drink_cost = MENU[user_drink_choice]['cost']
    ingredients_coffee = MENU[user_drink_choice]['ingredients']
    ingredients_in_tank = resources
    for key in ingredients_in_tank:
        if ingredients_coffee[key] > ingredients_in_tank[key]:
            print(f"Sorry there is not enough {key}")
            return (True, MENU, resources)
        else:
            continue
    user_money = money_process()
    if user_money < drink_cost:
        return (True, MENU, resources)
    else:
        print(f"Here is ${user_money - drink_cost} in change.")
        print("Here is your latte ☕. Enjoy!")
        for key in resources:
            resources[key] = resources[key] - ingredients_coffee[key]

        return (True, MENU, resources)
    # total_money = money_process()


def order(MENU, resources,money ):
    check = True
    while check:
        coffee_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
        if coffee_choice == "report":
            print_report(money)
        elif coffee_choice == "off":
            check = False
        else:
            check, MENU, resources = check_transaction_success(coffee_choice, MENU, resources)
            money +=  MENU[coffee_choice]['cost']
    print("The Coffee Machine is going to be turned off")
    return

money = 0
order(MENU, resources, money )
# TODO: 1. Print Report. print the amount of milk water and coffee in the machine.
# TODO: 2. Check resource is sufficient for making the dink.
# TODO: 3. Process the coins find out how much money the user has added
# TODO: 4. Check if the translation is successful
# TODO: 5. Make Coffee
