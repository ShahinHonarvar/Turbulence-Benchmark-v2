from itertools import permutations

def palindromes_between_indices(s):
    s = s[5:10].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        p = ''.join(perm)
        if p == p[::-1] and len(p) >= 4:
            palindromes.add(p)
    return palindromes