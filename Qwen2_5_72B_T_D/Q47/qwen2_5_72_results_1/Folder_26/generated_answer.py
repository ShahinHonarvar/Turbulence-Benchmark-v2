def palindromes_of_specific_lengths(s):
    s = s[24:85]
    s_lower = s.lower()
    palindromes = set()
    for length in range(21, 32):
        for start in range(len(s) - length + 1):
            substring = s_lower[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes