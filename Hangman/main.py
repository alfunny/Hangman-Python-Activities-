import random
import hangman_art
import hangman_words

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
# Delete this line: word_list = ["ardvark", "baboon", "camel"]
list_of_words = hangman_words.word_list
images_game = hangman_art.stages
logo_game = hangman_art.logo


index = random.randint(0, len(list_of_words)-1)
word = list_of_words[index]
word_convert = list(list_of_words[index])
contador = len(word_convert)
verification = bool(False)
verification_life = bool(True)
lives = 6
blank_space = []
for a in range(0, len(word_convert)):
    blank_space.append("_")

print("Welcome to:")
print(logo_game)
while not verification:
    if contador == 0:
        verification = True
        print("You win !!")

    elif lives == 0:
        verification = True
        print(f"You lose\nThe word was {word}")

    else:

        choose_char = input("Guess a letter:\n").lower()
        verification_life = True
        for i in range(0, len(word_convert)):

            if choose_char == word_convert[i]:
                blank_space[i] = choose_char
                contador -= 1
                verification_life = False

        if verification_life != False:
            print(images_game[lives-1])
            lives -= 1

        print(blank_space)
