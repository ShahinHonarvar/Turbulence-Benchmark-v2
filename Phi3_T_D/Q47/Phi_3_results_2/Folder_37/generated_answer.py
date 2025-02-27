def palindromes_of_specific_lengths(s):
    result = set()
    length = min(10, len(s))
    for i in range(length):
        for j in range(i + 3, min(i + 6, len + 1)):
            substring = s[i:j]
            if substring.isalpha() and len(substring) in [3, 4, 5] and (substring.lower() == substring[::-1].lower()):
                result.add(substring.lower())
    return result