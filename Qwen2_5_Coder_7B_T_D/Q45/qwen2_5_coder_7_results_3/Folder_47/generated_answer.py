def palindromes_between_indices(s):
    indices = s[3:8].lower()
    letters = sorted(set(indices))
    palindromes = set()
    for i in range(len(letters), 4, -1):
        for p in permutations(letters, i):
            if p == p[::-1]:
                palindromes.add(''.join(p))
    return palindromes