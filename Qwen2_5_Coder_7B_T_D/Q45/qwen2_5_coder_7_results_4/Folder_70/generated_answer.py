def palindromes_between_indices(s):
    s = s[1:7].lower()
    letters = set(s)
    palindromes = set()
    for length in range(4, len(s) + 1):
        for perm in permutations(letters, length):
            half = ''.join(perm[:length // 2])
            if length % 2 == 0:
                pal = half + half[::-1]
            else:
                pal = half + perm[length // 2] + half[::-1]
            if pal in s and pal not in palindromes:
                palindromes.add(pal)
    return palindromes