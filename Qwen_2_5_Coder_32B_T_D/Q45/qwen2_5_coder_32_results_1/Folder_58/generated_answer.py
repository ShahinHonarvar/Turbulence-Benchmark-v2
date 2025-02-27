from itertools import permutations

def palindromes_between_indices(s):
    s = ''.join(filter(str.isalpha, s[0:7])).lower()
    p = set()
    for perm in permutations(s):
        p.add(''.join(perm))
    palindromes = {x for x in p if len(x) >= 6 and x == x[::-1]}
    return palindromes