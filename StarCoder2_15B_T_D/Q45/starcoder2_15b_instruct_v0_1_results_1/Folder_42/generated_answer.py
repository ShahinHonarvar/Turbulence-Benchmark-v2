def palindromes_between_indices(s):
    s = s.lower()
    palindromes = set()
    for i in range(6, len(s) - 2):
        for j in range(i + 3, min(len(s), i + 10)):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes