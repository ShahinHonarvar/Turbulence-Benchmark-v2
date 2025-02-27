def palindromes_between_indices(s):
    subset = s[4:10]
    subset = ''.join(filter(str.isalpha, subset)).lower()
    unique_chars = set(subset)
    result = set()
    for r in range(3, len(unique_chars) + 1):
        for combination in combinations(unique_chars, r):
            perm = ''.join(permutations(combination))
            for p in perm:
                if p == p[::-1]:
                    result.add(p)
    return result