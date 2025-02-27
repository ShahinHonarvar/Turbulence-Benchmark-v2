def palindromes_between_indices(s):
    s = s[4:10]
    s = s.lower()
    letters = set(s)
    palindromes = set()
    for i in range(len(s), 6, -1):
        for j in range(len(s) - i + 1):
            substring = s[j:j + i]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes