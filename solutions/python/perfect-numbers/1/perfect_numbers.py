def classify(number):
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    if number == 1:
        return "deficient"

    aliquot_sum = 1

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            aliquot_sum += i
            if i != number // i:
                aliquot_sum += number // i

    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    else:
        return "deficient"