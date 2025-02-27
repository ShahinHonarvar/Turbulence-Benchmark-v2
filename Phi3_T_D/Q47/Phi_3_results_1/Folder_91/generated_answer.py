def palindromes_of_specific_lengths(s):
    s = s[:11].lower()
    palindromes = set()
    for length in range(3, 6):
        for start in range(11 - length + 1):
            substring = s[start:start + length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes