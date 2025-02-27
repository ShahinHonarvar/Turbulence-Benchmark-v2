from itertools import permutations

def palindromes_between_indices(s):
    segment = s[0:4].lower()
    palindromes = set()
    for perm in set(permutations(segment)):
        perm_str = ''.join(perm)
        if perm_str == perm_str[::-1] and len(perm_str) >= 4:
            palindromes.add(perm_str)
    return palindromes