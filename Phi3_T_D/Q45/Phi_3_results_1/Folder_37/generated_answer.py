from itertools import permutations

def palindromes_between_indices(s):
    start, end = (1, 4)
    letters = s[start - 1:end]
    letters_lower = set((c.lower() for c in letters if c.isalpha()))
    if len(letters_lower) < 5:
        return set()
    potential_palindromes = set((''.join(p) for p in permutations(letters_lower, 5)))
    return {p.upper() for p in potential_palindromes if p == p[::-1]}