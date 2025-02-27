from itertools import permutations

def palindromes_between_indices(s):
    substr = s[4:7].lower()
    unique_chars = ''.join(set(substr))
    perm_set = set([''.join(p) for p in permutations(unique_chars, 3)])
    result_set = set()
    for perm in perm_set:
        if len(perm) >= 2 and perm == perm[::-1]:
            result_set.add(perm + perm[::-1][1:])
            result_set.add(perm[0] + perm + perm[0])
    return result_set