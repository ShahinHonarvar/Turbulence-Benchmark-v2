def palindromes_between_indices(s):
    s = s[3:9].lower()
    letters = set(s)
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 5, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and len(substring) >= 5:
                palindromes.add(''.join(sorted(substring)))
    return palindromes