def palindromes_of_specific_lengths(s):
    s = s[34:91].lower()
    palindromes = set()
    for start in range(len(s) - 13):
        for end in range(start + 14, min(start + 40, len(s)) + 1):
            substring = s[start:end]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes