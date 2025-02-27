from itertools import permutations

def palindromes_between_indices(s):
    letters = set(s[1:7].lower())
    if len(letters) < 7:
        return set()
    perms = permutations(letters, 7)
    palindromes = set()
    for perm in perms:
        half = ''.join(perm[:3])
        if half == half[::-1]:
            palindromes.add(half + half[-2::-1])
    return palindromes