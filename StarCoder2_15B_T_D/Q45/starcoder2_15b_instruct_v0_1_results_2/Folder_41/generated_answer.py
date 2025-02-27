def palindromes_between_indices(s):
    s = s.lower()
    palindromes = set()
    for i in range(2, len(s) - 1):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                palindromes.add(s[i] + s[j])
    return palindromes