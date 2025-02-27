from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:9] if c.isalpha()]
    p = set(permutations(letters, 6))
    palindromes = {t for t in p if t == t[::-1]}
    return set((''.join(t) for t in palindromes))