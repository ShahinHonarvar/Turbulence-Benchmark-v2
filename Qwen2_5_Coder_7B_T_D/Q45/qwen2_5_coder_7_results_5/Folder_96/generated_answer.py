def palindromes_between_indices(s):
    s = s[3:9].lower()
    letters = ''.join(filter(str.isalpha, s))
    n = len(letters)
    if n < 6:
        return set()
    palindromes = set()
    for i in range(n):
        for j in range(i + 5, n + 1):
            word = letters[i:j]
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes