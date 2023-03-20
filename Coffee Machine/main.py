import menu

current_resources = menu.resources
machine_on = True
machine_bank = 0


def check_coins():
    global current_resources
    global drink_ingredients
    global drink_price
    global machine_on
    global choosen_drink
    global machine_bank

    print(f"Your coffee cost ${drink_price}\nPlease insert coins.")
    quarters = int(input("How many quarters?\n"))
    dimes = int(input("How many dimes?\n"))
    nickles = int(input("How many nickles?\n"))
    pennies = int(input("How many pennies?\n"))
    total_coins = (quarters*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01)

    if total_coins < drink_price:
        insert = round(drink_price-total_coins, 2)
        print("\n")
        print(
            f"You dont have enough coins\nYou need to insert ${insert} yet\n")
        machine_on = False
        return machine_on

    elif drink_price < total_coins:
        change = round(total_coins-drink_price, 2)
        print("\n")
        print(
            f"Have a good coffee!!!\nHere is your change ${change}\n")
        if choosen_drink == "espresso":
            current_resources["coffee"] -= drink_ingredients["coffee"]
            current_resources["water"] -= drink_ingredients["water"]
        else:
            current_resources["coffee"] -= drink_ingredients["coffee"]
            current_resources["water"] -= drink_ingredients["water"]
            current_resources["milk"] -= drink_ingredients["milk"]
        machine_bank += drink_price
    else:
        print("Have a good coffee!!\n")
        if choosen_drink == "espresso":
            current_resources["coffee"] -= drink_ingredients["coffee"]
            current_resources["water"] -= drink_ingredients["water"]
        else:
            current_resources["coffee"] -= drink_ingredients["coffee"]
            current_resources["milk"] -= drink_ingredients["milk"]
            current_resources["water"] -= drink_ingredients["water"]
        machine_bank += drink_price


def check_resources():
    global machine_on
    global drink_ingredients
    global current_resources
    global choosen_drink

    if choosen_drink == "espresso":
        if drink_ingredients["water"] > current_resources["water"]:
            print("Sorry!! there's not enough water\n")
            machine_on = False
            return machine_on
        elif drink_ingredients["coffee"] > current_resources["coffee"]:
            print("Sorry!! there's not enough coffee\n")
            machine_on = False
            return machine_on
    else:
        if drink_ingredients["water"] > current_resources["water"]:
            print("Sorry!! there's not enough water\n")
            machine_on = False
            return machine_on
        elif drink_ingredients["milk"] > current_resources["milk"]:
            print("Sorry!! there's not enough milk\n")
            machine_on = False
            return machine_on
        elif drink_ingredients["coffee"] > current_resources["coffee"]:
            print("Sorry!! there's not enough coffee\n")
            machine_on = False
            return machine_on


while machine_on:
    print("\n")
    choosen_drink = input(
        "What would you like? (espresso,latte,cappuccino)\n").lower()

    if choosen_drink == "report":
        print(current_resources)
        print(f"bank: ${machine_bank}\n")
        
    else:
        drink_ingredients = menu.MENU[choosen_drink]["ingredients"]
        drink_price = menu.MENU[choosen_drink]["cost"]

        resource_coffee = check_resources()
        if resource_coffee == False:
            break
        coins = check_coins()
