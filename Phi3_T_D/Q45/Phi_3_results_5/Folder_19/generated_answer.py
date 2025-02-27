from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:8]
    letters = ''.join((c for c in substring if c.isalpha()))
    letters_lower = letters.lower()
    palindromes = {''.join(p) for i in range(7, len(letters_lower) + 1) for p in permutations(letters_lower, i)}
    palindromes = {p for p in palindromes if p == p[::-1] and len(p) >= 7}
    return palindromes