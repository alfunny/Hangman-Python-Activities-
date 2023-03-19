from game_data import data
import art
import random


score = 0


def game_score():
    global score
    score += 1
    return score

# Função para escolhar o instagram aleatoriamente


def random_index():
    new_index = random.randint(0, 49)
    instagram = data[new_index]
    return instagram


on_game = True

while on_game:

    instagram_A = random_index()
    instagram_B = random_index()
    count_A = instagram_A['follower_count']
    count_B = instagram_B['follower_count']

# arte inicial da tela
    print(art.logo)
    print(
        f"Compare A: {instagram_A['name']}, a {instagram_A['description']}, from {instagram_A['country']}")
    print(art.vs)
    print(
        f"Against B: {instagram_B['name']}, a {instagram_B['description']}, from {instagram_B['country']}")

    player = input("Who has more followers? Type 'A' or 'B':\n")

# jogo

    if instagram_A['name'] == instagram_B['name']:
        instagram_A = random_index()
        count_A = instagram_A["follower_count"]

    elif count_A > count_B:
        if player == "A":
            print("You win !!!!\n")
            score = game_score()
        else:
            on_game = False

    else:
        if player == 'B':
            print("You win !!!\n")
            score = game_score()
        else:
            on_game = False
    print(f"A = {count_A}")
    print(f"B = {count_B}")
print("You lose")
print(score)
