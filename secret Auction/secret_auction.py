import os
from time import sleep
bids = {}

answer = 'yes'
while True:
    name = input("what is your name?: ")

    bids[name] = int(input("what is your bid amount: ").replace("$",""))

    answer = input("are there any other bidders? 'yes' or 'no': ").lower()

    if answer == 'no':
        print(f"{max(bids)} wins the silent bid!")
        break
    else:
        sleep(1)
        os.system('cls')