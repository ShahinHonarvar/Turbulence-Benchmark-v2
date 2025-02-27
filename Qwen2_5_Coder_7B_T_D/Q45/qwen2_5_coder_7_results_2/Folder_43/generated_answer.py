def palindromes_between_indices(s):
    letters = s[2:6].lower()
    letters = ''.join(filter(str.isalpha, letters))
    n = len(letters)
    if n < 4:
        return set()
    palindromes = set()
    for i in range(n - 3):
        for j in range(i + 3, n + 1):
            word = letters[i:j]
            if word == word[::-1]:
                for p in set(permutations(word)):
                    palindromes.add(''.join(p))
    return palindromes