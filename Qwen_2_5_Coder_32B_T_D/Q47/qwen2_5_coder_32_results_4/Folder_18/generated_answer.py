def palindromes_of_specific_lengths(s):
    s = s[11:84].lower()
    result = set()
    for start in range(len(s) - 12):
        for end in range(start + 12, min(start + 66, len(s)) + 1):
            substring = s[start:end]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result