def palindromes_between_indices(s):
    subset = s[6:9].lower()
    letters = set(subset)
    palindromes = set()
    for length in range(3, len(subset) + 1):
        for perm in set(permutations(letters, length)):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes