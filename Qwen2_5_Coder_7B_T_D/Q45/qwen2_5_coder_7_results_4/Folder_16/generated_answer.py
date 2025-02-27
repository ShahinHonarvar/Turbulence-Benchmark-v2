def palindromes_between_indices(s):
    subset = s[6:10]
    letters = set(subset.lower())
    result = set()
    for length in range(5, len(letters) + 1):
        for perm in permutations(letters, length):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                result.add(candidate)
    return result