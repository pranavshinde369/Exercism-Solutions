def find_anagrams(word, candidates):
    result = []

    target = sorted(word.lower())

    for candidate in candidates:
        if word.lower() != candidate.lower() and sorted(candidate.lower()) == target:
            result.append(candidate)

    return result
