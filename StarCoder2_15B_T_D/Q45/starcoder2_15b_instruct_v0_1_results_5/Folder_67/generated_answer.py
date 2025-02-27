def palindromes_between_indices(s):
    s_lower = s.lower()
    palindromes = set()
    for i in range(2, 7):
        for j in range(i + 1, 7):
            substring = s_lower[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes