def palindromes_between_indices(s):
    s = s[:7].lower()
    letters = ''.join(sorted(set(s)))
    n = len(letters)
    palindromes = set()
    for i in range(n - 2):
        for j in range(i + 2, n + 1):
            word = ''.join(letters[i:j])
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes