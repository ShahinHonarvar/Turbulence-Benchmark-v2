def palindromes_of_specific_lengths(s):
    s = s[23:95].lower()
    result = set()
    for start in range(len(s) - 16):
        for end in range(start + 17, min(start + 56, len(s)) + 1):
            substring = s[start:end]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result