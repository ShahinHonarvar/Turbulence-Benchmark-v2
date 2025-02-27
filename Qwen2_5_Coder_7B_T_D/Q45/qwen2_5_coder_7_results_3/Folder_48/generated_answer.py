def palindromes_between_indices(s):
    result = set()
    char_set = set(s[6:9].lower())
    if len(char_set) < 2:
        return result
    for char1 in char_set:
        for char2 in char_set:
            for char3 in char_set:
                for char4 in char_set:
                    candidate = char1 + char2 + char3 + char4
                    if candidate == candidate[::-1]:
                        result.add(candidate)
    return result