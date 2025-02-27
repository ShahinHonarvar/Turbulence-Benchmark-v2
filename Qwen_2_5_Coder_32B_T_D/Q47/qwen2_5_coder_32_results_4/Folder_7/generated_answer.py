def palindromes_of_specific_lengths(s):
    s = s[119:257].lower()
    result = set()
    for start in range(len(s) - 103):
        for end in range(start + 103, min(start + 123, len(s)) + 1):
            substring = s[start:end]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result