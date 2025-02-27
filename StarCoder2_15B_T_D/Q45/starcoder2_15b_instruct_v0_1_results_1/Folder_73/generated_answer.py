def palindromes_between_indices(s):
    s = s.lower()
    palindromes = set()
    for i in range(3, 7):
        for j in range(i + 1, 7):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes