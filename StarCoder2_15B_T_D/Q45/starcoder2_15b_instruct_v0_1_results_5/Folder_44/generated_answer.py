def palindromes_between_indices(s):
    s = s.lower()
    palindromes = set()
    for i in range(2, len(s) - 1):
        for j in range(i + 2, min(len(s), i + 7) + 1):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes