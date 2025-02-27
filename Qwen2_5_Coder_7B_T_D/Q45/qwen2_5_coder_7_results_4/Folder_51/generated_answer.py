def palindromes_between_indices(s):
    s = s[3:6].lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    for i in range(len(s), 2, -1):
        for comb in set(permutations(s, i)):
            if comb == comb[::-1]:
                palindromes.add(''.join(comb))
    return palindromes