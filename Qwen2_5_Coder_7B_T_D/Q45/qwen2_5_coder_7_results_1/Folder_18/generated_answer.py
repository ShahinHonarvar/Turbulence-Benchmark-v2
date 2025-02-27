def palindromes_between_indices(s):
    letters = s[1:7].lower()
    unique_letters = set(letters)
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for comb in itertools.permutations(unique_letters, length):
            candidate = ''.join(comb)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes