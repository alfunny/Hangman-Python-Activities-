from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
machine_on = True

while machine_on:

    choosen_drink = input(
        "What would you like? (espresso,latte,cappuccino)\n").lower()

    menu_item = menu.find_drink(choosen_drink)
    drink_cost = menu_item.cost
    enough_resource = coffee_maker.is_resource_sufficient(menu_item)

    if enough_resource == True:
        pay_here = money_machine.make_payment(drink_cost)
        if pay_here == True:
            coffee_maker.make_coffee(menu_item)
        else:
            machine_on = False
    else:
        machine_on = False
