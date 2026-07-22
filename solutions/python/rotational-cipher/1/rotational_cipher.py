def rotate(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            if char.islower():
                start = ord('a')
            else:
                start = ord('A')

            # Rotate the character
            shifted = (ord(char) - start + key) % 26 + start
            result += chr(shifted)
        else:
            # Keep spaces, punctuation, and numbers unchanged
            result += char

    return result