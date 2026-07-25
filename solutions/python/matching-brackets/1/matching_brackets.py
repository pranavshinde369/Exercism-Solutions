def is_paired(input_string):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    opening = set(pairs.values())

    for char in input_string:
        if char in opening:
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False

    return len(stack) == 0