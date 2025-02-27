def palindromes_of_specific_lengths(s):
    s_lower = s.lower()
    palindromes = set()
    for i in range(28, 95):
        for j in range(i + 38, i + 50):
            substring = s_lower[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes