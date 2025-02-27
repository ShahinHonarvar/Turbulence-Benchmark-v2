def palindromes_between_indices(s):
    letters = set(s[:5].lower())
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for letters_combination in itertools.permutations(letters, length):
            if letters_combination == letters_combination[::-1]:
                palindromes.add(''.join(letters_combination))
    return palindromes