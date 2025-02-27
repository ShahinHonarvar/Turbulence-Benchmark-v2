from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[1:9])).lower()
    l = len(letters)
    p = set()
    for i in range(6, l + 1):
        for perm in permutations(letters, i):
            t = ''.join(perm)
            if t == t[::-1]:
                p.add(t)
    return p