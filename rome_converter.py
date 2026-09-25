def to_roman(number: int) -> str:
    roman_numbers = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    result = ""

    for value, symbol in roman_numbers:
        while number >= value:
            result += symbol
            number -= value

    return result


def from_roman(roman: str) -> int:
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    roman = roman.upper()
    result = 0

    for index in range(len(roman)):
        current = values[roman[index]]

        if index + 1 < len(roman) and current < values[roman[index + 1]]:
            result -= current
        else:
            result += current

    return result
