def palindromes_between_indices(s):
    letters = s[2:10]
    letters = letters.lower()
    letters = ''.join(sorted(letters))
    n = len(letters)
    if n < 7:
        return set()
    palindromes = set()
    for i in range(n - 6):
        for j in range(i + 6, n + 1):
            substring = letters[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes