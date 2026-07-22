COLORS = [
    "black", "brown", "red", "orange", "yellow",
    "green", "blue", "violet", "grey", "white"
]

def label(colors):
    first = COLORS.index(colors[0])
    second = COLORS.index(colors[1])
    zeros = COLORS.index(colors[2])

    value = (first * 10 + second) * (10 ** zeros)

    if value >= 1000000000:
        return str(value // 1000000000) + " gigaohms"
    elif value >= 1000000:
        return str(value // 1000000) + " megaohms"
    elif value >= 1000:
        return str(value // 1000) + " kiloohms"
    else:
        return str(value) + " ohms"