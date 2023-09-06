MENU = {
    "mojito": {
        "ingredients": {
            "rum": 50,
            "lime juice": 30,
            "sugar syrup": 20,
            "mint leaves": 10,
            "soda water": 100,
        },
        "cost": 8.0,
    },
    "cosmopolitan": {
        "ingredients": {
            "vodka": 40,
            "cranberry juice": 60,
            "lime juice": 20,
            "triple sec": 20,
        },
        "cost": 9.0,
    },
    "margarita": {
        "ingredients": {
            "tequila": 50,
            "lime juice": 30,
            "triple sec": 20,
            "salt": 5,
        },
        "cost": 7.5,
    }
}

profit = 0
resources = {
    "rum": 500,
    "vodka": 400,
    "tequila": 300,
    "lime juice": 500,
    "sugar syrup": 200,
    "cranberry juice": 300,
    "triple sec": 200,
    "mint leaves": 100,
    "soda water": 400,
    "salt": 100,
}

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = float(input("Enter the total amount: $"))
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

def make_cocktail(cocktail_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {cocktail_name}. Enjoy!")

def print_report():
    """Prints a report of available resources and profit."""
    print("Current Resources:")
    for item, quantity in resources.items():
        print(f"{item.capitalize()}: {quantity}")
    print(f"Profit: ${profit}")

is_on = True

while is_on:
    choice = input("​What cocktail would you like? (mojito/cosmopolitan/margarita): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print_report()
    else:
        cocktail = MENU.get(choice)
        if cocktail is None:
            print("Invalid choice. Please try again.")
            continue
        if is_resource_sufficient(cocktail["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, cocktail["cost"]):
                make_cocktail(choice, cocktail["ingredients"])
