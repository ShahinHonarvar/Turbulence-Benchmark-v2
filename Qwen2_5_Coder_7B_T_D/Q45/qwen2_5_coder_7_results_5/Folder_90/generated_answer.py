def palindromes_between_indices(s):
    letters = s[:6].lower()
    unique_letters = set(letters)
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in set(itertools.permutations(unique_letters, length)):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes