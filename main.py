from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

items = Menu().get_items()
# report = CoffeeMaker().report()
work = True
while work:
    order = input(f"What would you like {items}: ")
    order = MenuItem(order)
    print(order)
    if order == "off":
        work = False
    elif order == "report":
        CoffeeMaker().report()
    else:
        sufficient = CoffeeMaker().is_resource_sufficient(order)
        print(sufficient)

