def palindromes_of_specific_lengths(s):
    s = s[20:75].lower()
    result = set()
    for start in range(len(s) - 35):
        for end in range(start + 36, min(start + 43, len(s)) + 1):
            substring = s[start:end]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result