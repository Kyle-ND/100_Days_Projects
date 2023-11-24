import os
from time import sleep
bids = {}

answer = 'yes'
while True:
    name = input("what is your name?: ")

    bids[name] = int(input("what is your bid amount: ").replace("$",""))

    answer = input("are there any other bidders? 'yes' or 'no': ").lower()
    print(bids)
    keys = bids.keys()
    if answer == 'no':
        print(f"{max(bids,key=bids.get)} wins the silent bid!")
        break
    else:
        sleep(1)
        os.system('clear')