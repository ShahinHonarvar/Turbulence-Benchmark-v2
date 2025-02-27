def palindromes_between_indices(s):
    s = s[3:8].lower()
    letters = ''.join(filter(str.isalpha, s))
    n = len(letters)
    if n < 5:
        return set()
    palindromes = set()
    for i in range(n - 4):
        for j in range(i + 4, n + 1):
            substring = letters[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes