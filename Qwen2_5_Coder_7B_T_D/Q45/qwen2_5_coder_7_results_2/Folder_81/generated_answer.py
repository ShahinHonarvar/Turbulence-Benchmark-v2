def palindromes_between_indices(s):
    s = s[:7].lower()
    letters = set(s)
    palindromes = set()
    for length in range(3, len(s) + 1):
        for perm in set(itertools.permutations(letters, length)):
            half = ''.join(perm[:length // 2])
            if length % 2 == 0:
                candidate = half + half[::-1]
            else:
                candidate = half + perm[length // 2] + half[::-1]
            if candidate == candidate[::-1] and candidate not in palindromes:
                palindromes.add(candidate)
    return palindromes