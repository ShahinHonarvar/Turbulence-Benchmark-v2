from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[7:10] if char.isalpha()]
    if len(letters) < 2:
        return set()
    perms = set(permutations(letters, 4))
    palindromes = set()
    for perm in perms:
        if perm == perm[::-1]:
            palindromes.add(''.join(perm))
    return palindromes