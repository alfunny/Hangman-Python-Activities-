from replit import clear
# OBS: I maid the code in replit,so i imported the clear method to use . Other option is to create a clear function to clean the console
 import logo


def adicao(first_number, second_number):
    return first_number + second_number


def multiple(first_number, second_number):
    return first_number * second_number


def division(first_number, second_number):
    return first_number / second_number


def subtracao(first_number, second_number):
    return first_number - second_number


print(logo)
answer = 0
verificator = True
while verificator:
    first_number = float(input("Chosse the first number?\n"))
    method = input("*\n/\n+\n-\nChosse a method?\n")
    second_number = float(input("Chosse the second number?\n"))
    if method == '+':
        answer = adicao(first_number, second_number)
    elif method == '-':
        answer = subtracao(first_number, second_number)
    elif method == '*':
        answer = round(multiple(first_number, second_number), 2)
    elif method == '/':
        answer = round(division(first_number, second_number), 2)
    print(f"{first_number} {method} {second_number} = {answer}")
    to_continue = input(
        "Do you want to use the calculator again? 'yes' or 'not'\n").lower()
    if to_continue == 'yes':
        clear()
    else:
        print("Goodbye!!\n")
        verificator = False
