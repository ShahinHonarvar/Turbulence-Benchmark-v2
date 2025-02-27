def palindromes_between_indices(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 6):
        for j in range(i + 7, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes