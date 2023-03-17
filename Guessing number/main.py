# guessing number game
import random
from art import logo

computer_number = random.randint(1, 100)
print(logo)
chosen_level = input("Do you want to play on easy or hard mode?\n")


if chosen_level == "easy":
    tentativas = 10
    for _ in range(1, 11):
        print("\n")
        player_number = int(input("which number you choose?\n"))
        if player_number > computer_number:
            print("too high, try again")
            tentativas -= 1
        elif player_number < computer_number:
            print("too low, try again")
            tentativas -= 1
        else:
            print(f"That's correct, the number is {computer_number}")
            break
    if tentativas == 0:
        print(f"you lost, the number is {computer_number}")
else:
    tentativas = 5
    for _ in range(1, 6):
        print("\n")
        player_number = int(input("which number you choose?\n"))
        if player_number > computer_number:
            print("too high, try again")
            tentativas -= 1
        elif player_number < computer_number:
            print("too low, try again")
            tentativas -= 1
        else:
            print(f"That's correct, the number is {computer_number}")
            break
    if tentativas == 0:
        print(f"you lost, the number is {computer_number}")
