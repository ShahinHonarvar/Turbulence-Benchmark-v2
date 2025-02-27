def palindromes_of_specific_lengths(s):
    s = s[155:284].lower()
    palindromes = set()
    for start in range(len(s) - 103):
        for end in range(start + 103, min(start + 120, len(s)) + 1):
            substring = s[start:end]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes