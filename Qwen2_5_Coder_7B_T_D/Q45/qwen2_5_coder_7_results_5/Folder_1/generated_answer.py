def palindromes_between_indices(s):
    letters = s[4:8].lower()
    letters_set = set(letters)
    palindromes = set()
    for i in range(5, len(letters) + 1):
        for combination in set(itertools.permutations(letters, i)):
            if combination == combination[::-1]:
                palindromes.add(''.join(combination))
    return palindromes