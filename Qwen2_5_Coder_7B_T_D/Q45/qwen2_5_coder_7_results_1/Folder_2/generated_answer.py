from itertools import permutations

def palindromes_between_indices(s):
    letters = s[1:6].lower()
    if len(letters) < 6:
        return set()
    palindromes = set()
    for perm in permutations(letters):
        half = ''.join(perm[:3])
        full = half + half[::-1]
        if len(full) >= 6:
            palindromes.add(full)
    return palindromes