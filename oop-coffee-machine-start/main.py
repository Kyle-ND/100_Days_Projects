from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    menu = Menu()
    machine = CoffeeMaker()
    M_machine = MoneyMachine()

    order = input("What would you like?: ")

    while True:
        exists = menu.find_drink(order)
        
        if exists:
            response = machine.is_resource_sufficient(exists)
            if response == True:
                machine.make_coffee(exists)
                break
            else:
                order = input(f"try something that needs less resources {menu.get_items()} : ")
        else:
            order = input(f"Try something on our menu: {menu.get_items()} : ")
        
def get_money():
    M_machine = MoneyMachine()


if __name__ == "__main__":
    main()