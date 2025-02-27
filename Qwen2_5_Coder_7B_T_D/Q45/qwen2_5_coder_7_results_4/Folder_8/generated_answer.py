def palindromes_between_indices(s):
    s = s[1:6].lower()
    letters = set(s)
    palindromes = set()
    for length in range(5, len(s) + 1):
        for combination in set(itertools.combinations(letters, length)):
            word = ''.join(combination)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes