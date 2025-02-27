def palindromes_of_specific_lengths(s):
    s = s[21:63].lower()
    palindromes = set()
    for length in range(22, 34):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes