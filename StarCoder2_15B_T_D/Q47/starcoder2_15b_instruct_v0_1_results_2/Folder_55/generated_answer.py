def palindromes_of_specific_lengths(s):
    s_lower = s.lower()
    palindromes = set()
    for length in range(10, 21):
        for start in range(10, 76 - length + 1):
            substring = s_lower[start:start + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes