from itertools import permutations

def palindromes_between_indices(s):
    letters = s[4:10].lower()
    palindromes = set()
    valid_perms = set((''.join(p) for p in set(permutations(letters, 6))))
    for perm in valid_perms:
        if perm == perm[::-1]:
            palindromes.add(perm)
    return palindromes