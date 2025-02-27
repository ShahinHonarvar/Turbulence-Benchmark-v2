from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 9:
        return set()
    sub = s[4:9]
    chars = ''.join(sorted((c.lower() for c in set(sub) if c.isalpha())))
    unique_chars = len(chars)
    if unique_chars < 2:
        return set()
    palindromes = {''.join(p) for p in permutations(chars) if ''.join(p) == ''.join(p)[::-1]}
    return set([p[:4] + p + p[:4] for p in palindromes if len(p) >= 4])