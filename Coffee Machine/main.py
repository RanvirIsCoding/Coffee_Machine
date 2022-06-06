from menu import MENU, resources, units
from art import logo


# TODO 4: Check resources sufficient?
def enough_resources(drink):
    required_resources = MENU[drink]["ingredients"]
    check_against = resources
    sufficient = True

    for resource in resources:
        if required_resources[resource] > check_against[resource]:
            insufficient_resource = resource
            sufficient = False

    if sufficient:
        process_transaction(drink)
    else:
        print(f"The machine does not have sufficient {insufficient_resource} to make a/an {drink}")
        input("Press enter to try again: ")
        make_coffee()


# TODO 5: Process coins.
def process_transaction(drink):
    cost_of_drink = MENU[drink]["cost"]

    print(f"That will be ${cost_of_drink}")
    total_pennies = int(input("Insert any number of pennies: "))
    total_nickels = int(input("Insert any number of nickels: "))
    total_dimes = int(input("Insert any number of dimes: "))
    total_quarters = int(input("Insert any number of quarters: "))
    successful = True

    total_money_submitted = total_pennies * 0.01 + total_nickels * 0.05 + total_dimes * 0.1 + total_quarters * 0.25

    # TODO 6: Check transaction successful?
    if cost_of_drink < total_money_submitted:
        change_to_return = round(total_money_submitted - cost_of_drink, 2)
        print(f"Here's the change, ${change_to_return} \nEnjoy your coffee ☕.")
        resources["money"] += cost_of_drink
        input("Press enter for choosing another drink: ")
    elif cost_of_drink == total_money_submitted:
        print("Woah, you certainly know your math. \nEnjoy your coffee ☕.")
        resources["money"] += cost_of_drink
        input("Press enter for choosing another drink: ")
    else:
        print(f"Insufficient money, transaction has been canceled. \nHere's your ${total_money_submitted}")
        successful = False

    # TODO 7: Make Coffee.
    if successful:
        for resource in resources:
            resources[resource] -= MENU[drink]["ingredients"][resource]
        make_coffee()
    else:
        make_coffee()


def make_coffee():
    print(logo)

    # TODO 1: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    choice = input("What would you like? A latte, espresso or cappuccino: ").lower()

    if choice == "latte" or choice == "espresso" or choice == "cappuccino":
        enough_resources(choice)
    # TODO 2: Turn off the Coffee Machine by entering “off” to the prompt.
    elif choice == "off":
        print("Coffee machine turning off...")
        return
    # TODO 3: Print report.
    elif choice == "report":
        for resource in resources:
            print(f"{resource.title()}: {resources[resource]} {units[resource]}")
        input("Press enter to return to home screen: ")
        make_coffee()
    else:
        input("Unknown command,Press enter try again: ")
        make_coffee()


make_coffee()
