def palindromes_between_indices(s):
    s_lower = s.lower()
    palindromes = set()
    for i in range(2, 10):
        for j in range(i + 3, len(s_lower) + 1):
            substring = s_lower[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes