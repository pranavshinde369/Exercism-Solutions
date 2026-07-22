COLOR_CODES = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}

TOLERANCE = {
    "grey": "0.05%",
    "violet": "0.1%",
    "blue": "0.25%",
    "green": "0.5%",
    "brown": "1%",
    "red": "2%",
    "gold": "5%",
    "silver": "10%"
}


def resistor_label(colors):

    # One-band resistor
    if len(colors) == 1:
        return "0 ohms"

    # Four-band resistor
    if len(colors) == 4:
        value = (
            COLOR_CODES[colors[0]] * 10 +
            COLOR_CODES[colors[1]]
        )
        value *= 10 ** COLOR_CODES[colors[2]]
        tolerance = TOLERANCE[colors[3]]

    # Five-band resistor
    else:
        value = (
            COLOR_CODES[colors[0]] * 100 +
            COLOR_CODES[colors[1]] * 10 +
            COLOR_CODES[colors[2]]
        )
        value *= 10 ** COLOR_CODES[colors[3]]
        tolerance = TOLERANCE[colors[4]]

    # Convert to proper unit
    if value >= 1_000_000_000:
        value = value / 1_000_000_000
        unit = "gigaohms"
    elif value >= 1_000_000:
        value = value / 1_000_000
        unit = "megaohms"
    elif value >= 1_000:
        value = value / 1_000
        unit = "kiloohms"
    else:
        unit = "ohms"

    return f"{value:g} {unit} ±{tolerance}"