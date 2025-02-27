def palindromes_between_indices(s):
    s = s.upper()
    palindromes = set()
    for i in range(len(s) - 7):
        for j in range(i + 6, len(s)):
            window = s[i:j + 1]
            if window == window[::-1]:
                palindromes.add(window)
    return palindromes