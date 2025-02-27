def palindromes_of_specific_lengths(s):
    palindromes = set()
    s_lower = s.lower()
    for length in range(29, 63):
        for i in range(11, len(s_lower) - length + 1):
            substring = s_lower[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes