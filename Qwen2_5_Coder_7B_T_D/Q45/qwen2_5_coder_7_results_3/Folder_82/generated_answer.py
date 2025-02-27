def palindromes_between_indices(s):
    s = s[1:7].lower()
    letters = ''.join(filter(str.isalpha, s))
    n = len(letters)
    if n < 7:
        return set()
    palindromes = set()
    for i in range(n - 6):
        for j in range(i + 6, n + 1):
            word = letters[i:j]
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes