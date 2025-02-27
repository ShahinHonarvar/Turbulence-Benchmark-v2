from itertools import permutations

def palindromes_between_indices(s):
    chars = s[4:9].lower()
    char_permutations = set([''.join(p) for p in permutations(chars)])
    palindromes = set()
    for perm in char_permutations:
        if len(perm) >= 3 and perm == perm[::-1]:
            palindromes.add(perm)
    return palindromes