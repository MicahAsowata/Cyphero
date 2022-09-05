def cyphero(plain_text: str, key: int):
    alphabet: list[str] = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']

    splitted_plain_text: list[str] = list(plain_text)
    for letter in splitted_plain_text:

        if letter != ' ':
            if letter in alphabet:
                index_of_letter: int = alphabet.index(letter) + 1
                cipher_text: int = index_of_letter + key

                if cipher_text >= len(alphabet):
                    difference: int = cipher_text % len(alphabet)
                    print(alphabet[difference], end='')
                else:
                    print(alphabet[cipher_text], end='')

        print(' ')