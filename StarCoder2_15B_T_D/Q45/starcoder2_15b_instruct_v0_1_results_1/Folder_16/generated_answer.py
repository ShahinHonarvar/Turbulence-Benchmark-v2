def palindromes_between_indices(s):
    s = s.lower()
    palindromes = set()
    for i in range(6, len(s) - 4):
        for j in range(i + 5, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes