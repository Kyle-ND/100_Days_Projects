from CData import data
import random
import os
from HL_art import log
from HL_art import v
def main():
    score = 0
    A = get_account()
    B = get_account()
    while True:
        os.system('cls')
        print(log)
        print(f"Score: {score}")
        print(f"Compare A: {A['name']} a {A['description']}")
        print(v)
        print(f"Against B: {B['name']} a {B['description']}")
        answer = input("Who has more followers? type A or B: ").upper()
        if answer == "A" and A['follower_count'] > B['follower_count']:
            score += 1
            A = B
            B = get_account()
            while A == B:
                B = get_account()
        elif answer == "B" and B['follower_count'] > A['follower_count']:
            score += 1
            A = B
            B = get_account()
            while A == B:
                B = get_account()
        else:
            print("Wrong!")
            print(f"Your score is: {score}")
            break

def get_account():
    acc = random.choice(data)

    return acc

if __name__ == "__main__":
    main()