"""
функция для сложения двух чисел типа float
args:
    a: float - первое число
    b: float - второе число
returns:
    float - сумма двух чисел
"""


def add_numbers(a: float, b: float) -> float:
    return a + b


print(add_numbers(1.5, 2.5) == 4.0)
