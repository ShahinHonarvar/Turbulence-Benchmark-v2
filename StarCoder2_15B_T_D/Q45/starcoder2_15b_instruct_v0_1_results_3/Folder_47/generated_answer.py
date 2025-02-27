def palindromes_between_indices(s):
    s = s.lower()
    palindromes = set()
    for i in range(3, 8):
        for j in range(i, 8):
            substring = s[i:j + 1]
            if len(substring) >= 5 and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes