import random

# a lista vazia de cada jogador sera o seu deck
player_deck = []
bot_deck = []

# gerar as cartas iniciais do player
for deck in range(0, 2):
    cartas_player1 = random.randint(1, 10)
    player_deck.append(cartas_player1)

# gerar as cartas iniciais do bot
for deck in range(0, 2):
    cartas_bot = random.randint(1, 10)
    bot_deck.append(cartas_bot)

####################### Player #######################################

# tratar o Às do player quando ele aparece no inicio
exist_1 = 1 in player_deck

if exist_1:
    index_1 = player_deck.index(1)
    player_deck[index_1] = 11

# duas primeiras cartas do player
print(f"This is your initial deck {player_deck}\n")

# loop pro player criar seu deck de cartas
add_card = True

while add_card:
    score_player = sum(player_deck)
    if score_player == 21:
        print("Blackjack!!!!! you win\n")
        add_card = False

    elif score_player > 21:
        print("You lost !!!!\n")
        add_card = False

    else:
        add = input("Do you want a new card? Type Y to add or N to stop\n")
        print("\n")
        if add == "Y":
            new_card = random.randint(1, 10)

            # tratar o Às quando a soma dos algarismos é menor que 11 e sair o 1 no sorteio
            if score_player < 11 and new_card == 1:
                new_card = 11

            player_deck.append(new_card)
            score_player = sum(player_deck)
            print(player_deck, score_player)
        else:
            add_card = False

############################ Bot ###########################

# duas primeiras cartas do bot
print("\n")
print(f"Bot initial deck {bot_deck}\n")

# tratar o Às do bot quando ele aparece no inicio
exist_1bot = 1 in bot_deck

if exist_1bot:
    index_1bot = bot_deck.index(1)
    bot_deck[index_1bot] = 11

# tratar as cartas para o deck do bot
score_bot = sum(bot_deck)
while score_bot <= 16 and score_player < 21:
    new_card_bot = random.randint(1, 10)
    if score_bot < 11 and new_card_bot == 1:
        new_card_bot = 11

    bot_deck.append(new_card_bot)
    score_bot = sum(bot_deck)

    print(bot_deck, score_bot)

################# Score final ############################
