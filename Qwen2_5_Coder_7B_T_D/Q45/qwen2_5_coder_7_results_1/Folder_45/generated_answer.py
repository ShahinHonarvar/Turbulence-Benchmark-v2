def palindromes_between_indices(s):
    s = s[5:10]
    s = ''.join(filter(str.isalpha, s)).lower()
    letters = list(s)
    letters.sort()
    n = len(letters)
    palindromes = set()
    for i in range(n):
        for j in range(i + 3, n + 1):
            word = ''.join(letters[i:j])
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes