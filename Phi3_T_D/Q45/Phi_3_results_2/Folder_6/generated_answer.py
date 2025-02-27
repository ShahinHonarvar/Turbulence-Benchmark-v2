from itertools import permutations

def palindromes_between_indices(s):
    for i in range(4, 8):
        sub_str = s[0:7]
        perms = set((''.join(p) for p in permutations(sub_str)))
        palindromes = {p[:i] + p[i - 1::-1] for p in perms if ''.join(p[:i]).lower() == ''.join(p[i - 1::-1]).lower()}
        if palindromes:
            return palindromes
    return set()