def palindromes_between_indices(s):
    s = s.lower()
    s = ''.join((c for c in s if c.isalpha()))
    palindromes = set()
    for i in range(3, 8):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if len(substring) >= 5 and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes