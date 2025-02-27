from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:7] if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        p = ''.join(perm)
        if p == p[::-1] and len(p) >= 4:
            palindromes.add(p)
    return palindromes