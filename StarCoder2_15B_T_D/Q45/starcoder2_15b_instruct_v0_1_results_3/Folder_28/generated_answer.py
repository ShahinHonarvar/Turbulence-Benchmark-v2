def palindromes_between_indices(s):
    s = s.lower()
    palindromes = set()
    for i in range(1, len(s) - 5):
        for j in range(i + 4, len(s)):
            if s[i:j + 1] == s[i:j + 1][::-1]:
                palindromes.add(s[i:j + 1])
    return palindromes