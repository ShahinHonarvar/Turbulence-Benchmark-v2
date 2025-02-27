def palindromes_between_indices(s):
    subset = s[2:9].lower()
    unique_chars = set(subset)
    result = set()
    for i in range(len(unique_chars), 6, -1):
        for comb in itertools.combinations(unique_chars, i):
            perm = ''.join(comb)
            if perm == perm[::-1]:
                result.add(perm)
    return result