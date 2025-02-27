def palindromes_between_indices(s):
    subset = s[3:8].lower()
    letters = list(subset)
    palindromes = set()
    n = len(letters)
    for i in range(n):
        for j in range(i + 3, n + 1):
            candidate = ''.join(letters[i:j])
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes