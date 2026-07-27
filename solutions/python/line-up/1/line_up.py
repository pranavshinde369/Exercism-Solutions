def line_up(name, number):
    if 10 <= number % 100 <= 20:
        suffix = "th"
    else:
        last = number % 10
        if last == 1:
            suffix = "st"
        elif last == 2:
            suffix = "nd"
        elif last == 3:
            suffix = "rd"
        else:
            suffix = "th"

    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"
