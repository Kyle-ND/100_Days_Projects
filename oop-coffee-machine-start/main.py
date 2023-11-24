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
                funds = get_money(exists.cost)
                if funds:
                    machine.make_coffee(exists)
                    break
                else:
                    pass
            else:
                order = input(f"try something that needs less resources {menu.get_items()} : ")
        else:
            order = input(f"Try something on our menu: {menu.get_items()} : ")
        
def get_money(cost):
    M_machine = MoneyMachine()
    M_machine.report()
    M_machine.process_coins()
    status = M_machine.make_payment(cost)
    if status == True:
        return status
    else:
        return status

if __name__ == "__main__":
    main()