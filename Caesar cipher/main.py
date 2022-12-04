import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)


def encrypt(text_f, shift):
    index = 0
    index_add = 0
    number_alphabet = len(alphabet)
    original_text = list(text_f)
    list_encrypted = [None] * len(original_text)

    while number_alphabet != 0:
        for i in range(0, len(original_text)):
            a = index + shift
            letra_original = alphabet[index]

            if original_text[i] in alphabet:

                if a >= len(alphabet) and letra_original == original_text[i]:
                    index_add = a - len(alphabet)
                    d = alphabet[index_add]  # letra shiftada
                    list_encrypted[i] = d

                elif letra_original == original_text[i]:
                    letra_shiftada = alphabet[a]
                    list_encrypted[i] = letra_shiftada
            else:
                list_encrypted[i] = original_text[i]

        number_alphabet -= 1
        index += 1

    crypt_word = "".join(list_encrypted)
    print(f"The encode of {text} is {crypt_word}")


def decrypt(text_d, shift):
    index = 0
    original_text = list(text_d)
    number_alphabet = len(alphabet)

    list_encrypted = [None] * len(original_text)

    while number_alphabet != 0:

        for i in range(0, len(original_text)):

            a = index - shift
            letra_original = alphabet[index]

            if original_text[i] in alphabet:

                if a >= len(alphabet) and letra_original == original_text[i]:

                    d = alphabet[a]
                    list_encrypted[i] = d

                elif letra_original == original_text[i]:
                    letra_shiftada = alphabet[a]
                    list_encrypted[i] = letra_shiftada

            else:
                list_encrypted[i] = original_text[i]

        number_alphabet -= 1
        index += 1

    crypt_word = "".join(list_encrypted)
    print(letra_original)
    print(f"the decode of {text} is {crypt_word}")


to_continue = True
while to_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == 'encode':
        encrypt(text, shift)
        answer = input(
            "Type 'yes' if you want to go again. Otherwise, type 'no'\n")
        if answer == 'no':
            to_continue = False
            print("Goodbye !!!")

    elif direction == 'decode':
        decrypt(text, shift)
        answer = input(
            "Type 'yes' if you want to go again. Otherwise, type 'no'\n")
        if answer == 'no':
            to_continue = False
            print("Goodbye !!!")
