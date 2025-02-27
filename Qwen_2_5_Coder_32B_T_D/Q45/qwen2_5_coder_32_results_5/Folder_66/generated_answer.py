from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(sorted([c for c in s[:6] if c.isalpha()], key=lambda x: x.lower()))
    seen = set()
    palindromes = set()
    for perm in permutations(letters):
        p = ''.join(perm).lower()
        if p == p[::-1] and len(p) >= 5 and (p not in seen):
            palindromes.add(p)
            seen.add(p)
    return palindromes