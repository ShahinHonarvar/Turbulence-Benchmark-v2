from itertools import permutations

def palindromes_between_indices(s):
    s_filtered = ''.join([c for c in s[1:9] if c.isalpha()]).lower()
    palindromes = {''.join(p) for p in permutations(s_filtered, len(s_filtered)) if ''.join(p) == ''.join(reversed(p))}
    return {p for p in palindromes if len(p) >= 7}