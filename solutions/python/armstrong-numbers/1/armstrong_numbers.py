def is_armstrong_number(number):
    power = len(str(number))
    total = 0

    for digit in str(number):
        total += int(digit) ** power

    return total == number
