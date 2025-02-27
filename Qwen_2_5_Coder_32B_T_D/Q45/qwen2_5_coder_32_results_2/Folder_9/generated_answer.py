from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[:7])).lower()
    p = set()
    for perm in permutations(letters, 7):
        c = ''.join(perm)
        if c == c[::-1]:
            p.add(c)
    return p