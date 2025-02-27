def palindromes_between_indices(s):
    subset = s[3:8]
    subset = subset.lower()
    letters = sorted(subset)
    n = len(letters)
    palindromes = set()
    for i in range(n):
        for j in range(i + 3, n + 1):
            substring = ''.join(letters[i:j])
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes