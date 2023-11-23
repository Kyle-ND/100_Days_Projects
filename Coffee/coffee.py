import os
from time import sleep
import coffee_menu as menu

def main():
    print(menu.logo)
    coffees = menu.Coffees
    resources = menu.resources 
    while True:
        print("Machine Resources:")
        report(resources)
        order = get_order(coffees)
        report(resources)
        print("Checking resources.........")
        sleep(1)
        status,resources = check_resources(order,resources,coffees)
        if status:
             os.system('cls')
             print(f"Making your {order}......")
             sleep(1.5)
             report(resources)
             print("DONE ☕")
             print(menu.done)
             sleep(2)

        else:
            os.system('cls')
            print(f"!! not enough resources to make {order}")


def get_order(coffees):
    while True:
        order = input('What would you like to order?: ').lower()
        if order in coffees:
            return order
        else:
            os.system('cls')
            print(f"Sorry we do not serve '{order}' yet but try any of these:")
            print(list(coffees.keys()))

def report(resources):
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")

def check_resources(type_coffee,machine_resources,coffees):

    response = False
    if type_coffee == 'espresso':
      response,machine_resources = espresso(type_coffee,machine_resources,coffees)
      return response,machine_resources
    elif type_coffee == 'latte':
        response,machine_resources = latte(type_coffee,machine_resources,coffees)
        return response,machine_resources
    elif type_coffee == 'cappuccino':
        response,machine_resources = cappuccino(type_coffee,machine_resources,coffees)
        return response,machine_resources


def espresso(type_coffee,machine_resources,coffees):

    drink = coffees['espresso']['ingredients']
    if machine_resources['water'] >= drink['water']:
            if machine_resources['coffee'] >= drink['coffee']:
                print(f'An {type_coffee} Costs ${coffees[type_coffee]['cost']}')
                coins = get_coins(coffees[type_coffee]['cost'])
                machine_resources['water'] -= drink['water']
                machine_resources['coffee'] -= drink['coffee']
                return True,machine_resources
            else:
                 return False
    else:
         return False
    
def latte(type_coffee,machine_resources,coffees):

    drink = coffees['latte']['ingredients']
    if machine_resources['water'] >= drink['water']:
            if machine_resources['coffee'] >= drink['coffee']:
                if machine_resources['milk'] >= drink['milk']:
                    print(f'A {type_coffee} Costs ${coffees[type_coffee]['cost']}')
                    coins = get_coins(coffees[type_coffee]['cost'])
                    machine_resources['water'] -= drink['water']
                    machine_resources['coffee'] -= drink['coffee']
                    machine_resources['milk'] -= drink['milk']
                    return True,machine_resources
                else:
                    return False
            else:
                 return False
    else:
         return False
    

def cappuccino(type_coffee,machine_resources,coffees):

    drink = coffees['cappuccino']['ingredients']
    if machine_resources['water'] >= drink['water']:
            if machine_resources['coffee'] >= drink['coffee']:
                if machine_resources['milk'] >= drink['milk']:
                    print(f'A {type_coffee} Costs ${coffees[type_coffee]['cost']}')
                    coins = get_coins(coffees[type_coffee]['cost'])
                    machine_resources['water'] -= drink['water']
                    machine_resources['coffee'] -= drink['coffee']
                    machine_resources['milk'] -= drink['milk']

                    return True,machine_resources
                else:
                    return False
            else:
                 return False
    else:
         return False


def get_coins(cost):
    valid_coins = ["0.25","0.05","0.10","0.01"]
    coins = 0
    while True:
         coin = input("insert coin: ")
         if coin in valid_coins:
              coin = float(coin)
              coins += coin
              if coins == cost or coins > float(cost):
                   return coins
              else:
                   print(f"Balance: {round(float(cost)-coins,2)}")
                   pass
         else:
              print("Invalid coin")
              print(valid_coins)
              print(f"Balance: {round(float(cost)-coins,2)}")
                   
              

if __name__ == '__main__':
    main()

