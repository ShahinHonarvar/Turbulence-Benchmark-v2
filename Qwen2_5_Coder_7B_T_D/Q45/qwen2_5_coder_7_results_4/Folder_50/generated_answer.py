def palindromes_between_indices(s):
    letters = s[4:9]
    letters = ''.join(filter(str.isalpha, letters.lower()))
    n = len(letters)
    if n < 5:
        return set()
    palindromes = set()
    for i in range(n - 4):
        for j in range(i + 5, n + 1):
            word = letters[i:j]
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes