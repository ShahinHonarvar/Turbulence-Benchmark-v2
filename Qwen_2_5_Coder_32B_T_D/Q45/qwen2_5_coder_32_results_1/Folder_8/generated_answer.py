from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[1:6] if c.isalpha()]
    letters = [c.lower() for c in letters]
    palindromes = set()
    for perm in permutations(letters):
        p = ''.join(perm)
        if p == p[::-1] and len(p) >= 5:
            palindromes.add(p)
    return palindromes