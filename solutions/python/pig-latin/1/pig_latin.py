def translate(text):
    result = []

    for word in text.split():

        if word.startswith(("a", "e", "i", "o", "u", "xr", "yt")):
            result.append(word + "ay")
            continue

        i = 0
        while True:
            if word[i] in "aeiou":
                break
            if word[i] == "y" and i != 0:
                break
            if word[i:i+2] == "qu":
                i += 2
                break
            i += 1

        result.append(word[i:] + word[:i] + "ay")

    return " ".join(result)