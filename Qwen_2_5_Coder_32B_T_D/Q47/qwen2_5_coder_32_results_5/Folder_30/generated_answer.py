def palindromes_of_specific_lengths(s):
    s = s[14:91].lower()
    palindromes = set()
    for start in range(len(s) - 54):
        for length in range(55, 72):
            substring = s[start:start + length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes