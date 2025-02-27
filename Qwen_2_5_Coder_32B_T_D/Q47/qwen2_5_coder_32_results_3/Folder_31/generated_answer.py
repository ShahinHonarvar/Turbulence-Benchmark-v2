def palindromes_of_specific_lengths(s):
    result = set()
    s = s[11:84].lower()
    for start in range(len(s) - 36):
        for end in range(start + 37, min(start + 61, len(s)) + 1):
            substring = s[start:end]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result