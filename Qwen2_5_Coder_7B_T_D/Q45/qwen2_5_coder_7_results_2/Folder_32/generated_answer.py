def palindromes_between_indices(s):
    s = s[1:8].lower()
    letters = set(s)
    palindromes = set()
    for i in range(5, len(s) + 1):
        for combination in set(permutations(letters, i)):
            if combination == combination[::-1]:
                palindromes.add(''.join(combination))
    return palindromes