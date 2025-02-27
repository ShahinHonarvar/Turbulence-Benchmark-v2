def palindromes_between_indices(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 6):
        for j in range(i + 6, len(s)):
            substring = s[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes