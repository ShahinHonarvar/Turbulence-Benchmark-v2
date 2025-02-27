def palindromes_between_indices(s):
    letters = s[1:5].lower()
    letters = ''.join(sorted(letters))
    n = len(letters)
    palindromes = set()
    for i in range(n - 4):
        for j in range(i + 4, n + 1):
            substring = letters[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes