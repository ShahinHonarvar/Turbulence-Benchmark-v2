def palindromes_between_indices(s):
    subset = s[3:9]
    letters = set(subset.lower())
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for combination in itertools.combinations(letters, length):
            for perm in itertools.permutations(combination):
                word = ''.join(perm)
                if word == word[::-1]:
                    palindromes.add(word)
    return palindromes