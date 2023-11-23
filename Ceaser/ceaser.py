
from ceaser_art import logo

def main():

    alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u","v", "w", "x", "y","z"]
    options = ("encrypt", "decrypt",)
    print(logo)
    while True:
        try:

            direction = input("would you like to encrypt or decrypt your message?: ").lower()
            if direction in options:
                text = input("Type your message: ").lower()
                shift = int(input("Type the shift number:\n"))
                encrypted = ceaser(text, shift,alphabets,direction)
                print(f"Here is your message encrypted: {encrypted}")

            else:
                print("!! Did not quite get that try again with only encrypt or decrypt !!")
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

        except ValueError:
            exit("please enter a number as a shift value.")

def ceaser(text,shift,alphabets,direction):
    coded = ""
    if direction == "decrypt":
        shift *= -1
        
    for letter in text:
        new_letter = alphabets.index(letter) + shift

        if new_letter >= len(alphabets):
            coded += alphabets[new_letter - 26]
        else:
            coded += alphabets[new_letter]
    return coded

if __name__ == "__main__":
    main()



