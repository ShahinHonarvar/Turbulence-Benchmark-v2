def palindromes_of_specific_lengths(s):
    s = s[25:90]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for center in range(len(s)):
        for radius in range(1, min(len(s) - center, 32)):
            substring = s[center:min(center + radius * 2, len(s))]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes