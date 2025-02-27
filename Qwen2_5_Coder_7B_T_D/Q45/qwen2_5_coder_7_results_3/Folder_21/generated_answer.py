def palindromes_between_indices(s):
    letters = set(s[1:9].lower())
    palindromes = set()
    for i in range(len(letters), 7, -1):
        for perm in permutations(letters, i):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes