def palindromes_of_specific_lengths(s):
    s_lower = s.lower()
    palindromes = set()
    for i in range(10):
        for j in range(i + 3, min(i + 6, len(s_lower))):
            substring = s_lower[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes