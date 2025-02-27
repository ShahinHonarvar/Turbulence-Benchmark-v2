def palindromes_between_indices(s):
    letters = s[3:6]
    letters_lower = letters.lower()
    unique_letters = set(letters_lower)
    palindromes = set()
    for combination in permutations(unique_letters, 2):
        for perm in permutations(combination * 2):
            candidate = ''.join(perm)
            if candidate == candidate[::-1] and len(candidate) >= 4:
                palindromes.add(candidate)
    return palindromes