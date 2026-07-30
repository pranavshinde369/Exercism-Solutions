def is_isogram(phrase):
    letters = set()

    for char in phrase.lower():
        if char.isalpha():
            if char in letters:
                return False
            letters.add(char)
    return True
