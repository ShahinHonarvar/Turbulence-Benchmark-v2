from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[7:10])).lower()
    pals = set()
    for perm in permutations(letters):
        p = ''.join(perm)
        if len(p) >= 3 and p == p[::-1]:
            pals.add(p)
    return pals