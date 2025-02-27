from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:10].lower()
    palindromes = set()
    for length in range(7, len(substring) + 1):
        perms = {''.join(p) for p in permutations(substring, length)}
        for p in perms:
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes