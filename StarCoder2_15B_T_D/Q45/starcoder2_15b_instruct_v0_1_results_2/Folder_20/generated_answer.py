def palindromes_between_indices(s):
    s = s.lower()
    palindromes = set()
    for i in range(2, len(s) - 2):
        for j in range(i + 2, len(s) - 2):
            if s[i] == s[j] and s[i + 1] == s[j - 1]:
                palindromes.add(s[i:j + 1])
    return palindromes