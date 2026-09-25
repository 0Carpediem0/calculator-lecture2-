import secrets
import string


def generate_password(
    length: int, lowercase: bool, uppercase: bool, digits: bool, special_chars: bool
) -> str:
    char_groups = []
    if lowercase:
        char_groups.append(string.ascii_lowercase)
    if uppercase:
        char_groups.append(string.ascii_uppercase)
    if digits:
        char_groups.append(string.digits)
    if special_chars:
        char_groups.append(string.punctuation)

    if not char_groups:
        raise ValueError("Задайте хотя бы один тип символов для генерации пароля.")
    if length < len(char_groups):
        raise ValueError("Длина пароля меньше числа выбранных типов символов.")

    password = [secrets.choice(group) for group in char_groups]
    char_pool = "".join(char_groups)
    remaining_length = length - len(password)
    password.extend(secrets.choice(char_pool) for _ in range(remaining_length))
    secrets.SystemRandom().shuffle(password)
    return "".join(password)


print("Генератор паролей")
try:
    length = int(input("Введите длину пароля: "))
    lowercase = input("Использовать строчные буквы? (y/n): ").lower() == "y"
    uppercase = input("Использовать заглавные буквы? (y/n): ").lower() == "y"
    digits = input("Использовать цифры? (y/n): ").lower() == "y"
    special_chars = input("Использовать специальные символы? (y/n): ").lower() == "y"
    password = generate_password(
        length, lowercase, uppercase, digits, special_chars
    )
    print("Сгенерированный пароль:", password)
except ValueError as error:
    print("Ошибка:", error)
