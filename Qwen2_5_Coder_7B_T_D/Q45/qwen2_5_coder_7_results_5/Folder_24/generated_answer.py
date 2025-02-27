def palindromes_between_indices(s):
    s = s[2:10].lower()
    letters = sorted(set(s))
    palindromes = set()
    for i in range(len(letters), 3, -1):
        for p in permutations(letters, i):
            if p == p[::-1]:
                palindromes.add(''.join(p))
    return palindromes