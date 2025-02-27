def palindromes_between_indices(s):
    letters = s[6:10]
    letters = letters.lower()
    letters = ''.join(sorted(letters))
    n = len(letters)
    palindromes = set()
    for i in range(n - 2):
        for j in range(i + 2, n + 1):
            word = letters[i:j]
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes