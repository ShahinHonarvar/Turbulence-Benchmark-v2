def palindromes_of_specific_lengths(s):
    s_lower = s.lower()
    palindromes = set()
    for length in range(32, 35):
        for i in range(23, len(s_lower) - length + 1):
            substring = s_lower[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes