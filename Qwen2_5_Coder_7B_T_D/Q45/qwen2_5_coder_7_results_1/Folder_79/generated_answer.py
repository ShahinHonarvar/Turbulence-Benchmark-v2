def palindromes_between_indices(s):
    s = s[1:8].lower()
    letters = set(s)
    palindromes = set()
    for length in range(3, len(s) + 1):
        for combination in set(permutations(letters, length)):
            candidate = ''.join(combination)
            if candidate == candidate[::-1] and candidate not in palindromes:
                palindromes.add(candidate)
    return palindromes