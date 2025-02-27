def palindromes_between_indices(s):
    s = s.upper()[6:10]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 4, len(s) + 1):
            palindromes.add(s[i:j])
    return palindromes