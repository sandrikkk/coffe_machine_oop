from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker=CoffeeMaker()
money_machine = MoneyMachine()

machine = True
while machine:
    choice = input("Romeli Yava gindat ? (espresso/latte/cappuccino):")
    if choice == "report" or choice == "REPORT":
        coffee_maker.report()
    elif choice == "OFF" or choice == "off":
        machine=False
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)