from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:10] if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        p = ''.join(perm)
        if p == p[::-1] and len(p) >= 7:
            palindromes.add(p)
    return palindromes