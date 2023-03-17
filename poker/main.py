import random
import art
play_again = True
your_bank = 900
while play_again and your_bank > 0:
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

    score_player = sum(player_deck)
    score_bot = sum(bot_deck)

###################### Inicio ################################
    print(art.logo)
    print(
        f"This is your initial deck {player_deck} Score:{score_player} Bank:{your_bank}\n")

###################### Coins ####################################

    deal_deck = [1, 5, 25, 50, 100, 500]
    minus_coin = int(
        input("choose a price to deal (1,5,25,50,100,500)\n"))


####################### Player ###################################
# antes de tratar o player é preciso verificar se no deck inicial do bot nao tem o 21
    if score_bot == 21 and score_player < 21:
        print("You lose!!! the bot has a blackjack")
# tratar o Às do player quando ele aparece no inicio
    exist_1 = 1 in player_deck

    if exist_1:
        index_1 = player_deck.index(1)
        player_deck[index_1] = 11

# loop pro player criar seu deck de cartas
    add_card = True
    while add_card:

        score_player = sum(player_deck)
        if score_player == 21:
            print("Blackjack!!!!! you win\n")
            again = input("Do you want to try again?\n")
            if again == "N":
                play_again = False
            add_card = False
            your_bank += minus_coin
        elif score_player > 21:
            print("You lost !!!!\n")
            again = input("Do you want to try again?\n")
            if again == "N":
                play_again = False
            add_card = False
            your_bank -= minus_coin
        else:
            add = input("Do you want a new card? Type Y to add or N to stop\n")
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

# tratar o Às do bot quando ele aparece no inicio
    exist_1bot = 1 in bot_deck

    if exist_1bot:
        index_1bot = bot_deck.index(1)
        bot_deck[index_1bot] = 11

# duas primeiras cartas do bot
    print("\n")
    print(f"Bot initial deck {bot_deck}\n")

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
#score_player < 21
#
    if score_player < 21:
        if score_bot == score_player:
            print("\n")
            print(
                f"A tie!!!\nBot score:{score_bot}\nYour score:{score_player}\n")
            again = input("Do you want to try again?\n")
            if again == "N":
                play_again = False
        elif score_bot <= 21 and score_player < score_bot:
            print("\n")
            print(
                f"You lost!!!\nBot score:{score_bot}\nYour score:{score_player}\n")
            again = input("Do you want to try again?\n")
            if again == "N":
                play_again = False
            your_bank -= minus_coin
        else:
            print("\n")
            print(
                f"You Win !!!\nBot score:{score_bot}\nYour score:{score_player}\n")
            again = input("Do you want to try again?\n")
            if again == "N":
                play_again = False
            your_bank += minus_coin
