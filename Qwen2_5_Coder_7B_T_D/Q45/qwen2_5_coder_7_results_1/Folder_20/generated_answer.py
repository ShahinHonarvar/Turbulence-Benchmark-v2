def palindromes_between_indices(s):
    s = s[2:9].lower()
    letters = set(s)
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for comb in combinations(letters, length):
            perm = set(permutations(comb))
            for p in perm:
                if p == p[::-1]:
                    palindromes.add(''.join(p))
    return palindromes