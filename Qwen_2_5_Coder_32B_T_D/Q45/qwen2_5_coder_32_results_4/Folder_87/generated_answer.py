from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:10] if c.isalpha()]
    seen = set()
    palindromes = set()
    for perm in permutations(letters):
        p = ''.join(perm)
        if p in seen:
            continue
        seen.add(p)
        if p == p[::-1] and len(p) >= 3:
            palindromes.add(p)
    return palindromes