from itertools import permutations

def palindromes_between_indices(s):
    s = s[6:9].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        p = ''.join(perm)
        if len(p) >= 4 and p == p[::-1]:
            palindromes.add(p)
    return palindromes