def palindromes_between_indices(s):
    letters = s[2:5].lower()
    letters = ''.join(sorted(letters))
    n = len(letters)
    palindromes = set()
    for i in range(n):
        for j in range(i + 2, n + 1):
            substring = letters[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes