from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:6].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for p in permutations(letters, min(5, len(letters))):
        p = ''.join(p)
        if p == p[::-1] and len(p) == 5:
            palindromes.add(p)
    return palindromes