def palindromes_between_indices(s):
    s = s.lower()
    palindromes = set()
    for i in range(1, len(s) - 1):
        for j in range(i + 2, len(s)):
            if s[i] == s[j]:
                palindromes.add(s[i:j + 1])
    return palindromes