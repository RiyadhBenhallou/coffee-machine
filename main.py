from coffe_machine import resources, MENU


def is_resources_sufficient(drink):
    for item in drink['ingredients']:
        if resources[item] < drink['ingredients'][item]:
            return False
    return True

def process_payment():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

is_on = True
money = 0

while is_on:
    answer = input('Would you like Espresso/Latte/Cappuccino: ').lower()
    if answer == 'report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffe: {resources['coffee']}g\nMoney: {money}$")
    elif answer == 'off':
        is_on = False
        print("Turning off the coffee machine.")
    elif answer in MENU:
        drink = MENU[answer]
        if is_resources_sufficient(drink):
            payment = process_payment()
            if payment >= drink['cost']:
                change = payment - drink['cost']
                money += drink['cost']
                print(f"Here is your change: ${change:.2f}")
                for item in drink['ingredients']:
                    resources[item] -= drink['ingredients'][item]
            else:
                print("Not enough money inserted.")
        else:
            print("Not enough resources.")
    elif answer not in MENU:
        print("Invalid choice. Please try again.")



