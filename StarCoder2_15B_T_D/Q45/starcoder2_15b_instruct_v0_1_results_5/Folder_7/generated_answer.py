def palindromes_between_indices(s):
    s = s.lower()
    palindromes = set()
    for i in range(1, 10):
        for j in range(i + 6, len(s) - 9 + i):
            window = s[i:j + 1]
            if window == window[::-1]:
                palindromes.add(window)
    return palindromes