def palindromes_between_indices(s):
    subset = s[7:9]
    subset = subset.lower()
    unique_chars = set(subset)
    palindromes = set()
    for length in range(3, len(unique_chars) + 1):
        for combination in set(itertools.permutations(unique_chars, length)):
            candidate = ''.join(combination)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes