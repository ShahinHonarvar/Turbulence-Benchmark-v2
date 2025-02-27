def palindromes_between_indices(s):
    s = s.lower()
    palindromes = set()
    for i in range(2, 10):
        for j in range(i + 1, min(i + 7, len(s))):
            if s[i:j + 1] == s[i:j + 1][::-1]:
                palindromes.add(s[i:j + 1])
    return palindromes