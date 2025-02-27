def palindromes_between_indices(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 3):
        for j in range(i + 4, min(len(s), i + 6) + 1):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes