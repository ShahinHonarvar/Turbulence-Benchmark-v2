def palindromes_between_indices(s):
    subset = s[7:10].lower()
    unique_chars = set(subset)
    result = set()
    for char1 in unique_chars:
        for char2 in unique_chars:
            for char3 in unique_chars:
                for char4 in unique_chars:
                    for char5 in unique_chars:
                        for char6 in unique_chars:
                            for char7 in unique_chars:
                                for char8 in unique_chars:
                                    word = char1 + char2 + char3 + char4 + char5 + char6 + char7 + char8
                                    if word == word[::-1] and len(set(word)) >= 4:
                                        result.add(word)
    return result