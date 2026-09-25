from getpass import getpass


def hangman(word):
    word = word.lower()
    guessed_letters = []
    attempts = 6
    display_word = ["_" for _ in word]

    print("Игра началась!")
    print("У вас есть", attempts, "попыток, чтобы угадать слово.")

    while attempts > 0 and "_" in display_word:
        print("\nСлово: ", " ".join(display_word))
        guess = input("Введите букву: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Пожалуйста, введите одну букву.")
            continue

        if guess in guessed_letters:
            print("Вы уже вводили эту букву.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            human(attempts)
            print("Правильно!")
            for index, letter in enumerate(word):
                if letter == guess:
                    display_word[index] = guess
        else:
            attempts -= 1
            human(attempts)
            print("Неправильно! У вас осталось", attempts, "попыток.")

    if "_" not in display_word:
        print("\nПоздравляем! Вы угадали слово:", word)
    else:
        print("\nИгра окончена! Слово было:", word)


def human(attempts):
    if attempts == 6:
        print("""
    +---+
    |   |
        |
        |
        |
        |
=========""")
    elif attempts == 5:
        print("""
    +---+
    |   |
    0   |
        |
        |
        |
=========""")
    elif attempts == 4:
        print("""
    +---+
    |   |
    0   |
    |   |
    |   |
        |
=========""")
    elif attempts == 3:
        print("""
    +---+
    |   |
    0   |
    |-  |
    |   |
        |
=========""")
    elif attempts == 2:
        print("""
    +---+
    |   |
    0   |
   -|-  |
    |   |
        |
=========""")
    elif attempts == 1:
        print("""
    +---+
    |   |
    0   |
   -|-  |
    |   |
     \  |
=========""")
    elif attempts == 0:
        print("""
    +---+
    |   |
    0   |
   -|-  |
    |   |
   / \  |
=========""")


word = getpass("Введите слово для игры в виселицу: ")
while not word.isalpha():
    print("Пожалуйста, введите слово, состоящее только из букв.")
    word = getpass("Введите слово для игры в виселицу: ")
hangman(word)
