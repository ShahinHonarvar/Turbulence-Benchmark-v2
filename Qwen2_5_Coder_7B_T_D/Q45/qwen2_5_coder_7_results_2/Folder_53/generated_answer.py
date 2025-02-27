def palindromes_between_indices(s):
    subset = s[4:9]
    letters = set(subset.lower())
    result = set()
    for i in range(len(letters), 0, -1):
        for comb in itertools.combinations(letters, i):
            perm = ''.join(comb)
            half = perm[:i // 2]
            if i % 2 == 0:
                full = half + half[::-1]
            else:
                full = half + perm[i // 2] + half[::-1]
            if len(full) >= 6:
                result.add(full)
    return result