def palindromes_of_specific_lengths(s):
    s = s[18:66].lower()
    result = set()
    for start in range(len(s) - 22):
        for end in range(start + 23, min(start + 37, len(s)) + 1):
            substring = s[start:end]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result