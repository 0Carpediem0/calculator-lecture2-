def encoder(text, shift):
    rus_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    eng_alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for char in text:
        if char.isalpha():
            if char.lower() in rus_alphabet:
                alphabet = (
                    rus_alphabet.upper()
                    if char.isupper()
                    else rus_alphabet
                )
                position = alphabet.index(char)
                result += alphabet[(position + shift) % len(alphabet)]
            else:
                alphabet = (
                    eng_alphabet.upper()
                    if char.isupper()
                    else eng_alphabet
                )
                position = alphabet.index(char)
                result += alphabet[(position + shift) % len(alphabet)]
        else:
            result += char

    return result


def decoder(text, shift):
    return encoder(text, -shift)
