def palindromes_between_indices(s):
    s = s.lower()
    palindromes = set()
    for i in range(2, len(s) - 1):
        for j in range(i + 1, min(i + 8, len(s))):
            if s[i:j + 1] == s[i:j + 1][::-1]:
                palindromes.add(s[i:j + 1])
    return palindromes