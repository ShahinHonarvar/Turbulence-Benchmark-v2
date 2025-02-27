from itertools import permutations

def palindromes_between_indices(s):
    chars = ''.join((s[i].lower() for i in range(4, 6)))
    if len(chars) < 3:
        return set()
    palindromes = set((''.join(p) for p in permutations(chars) if p[0].isalpha() and p[-1].isalpha() and (p[0].lower() == p[-1].lower())))
    return {p for p in palindromes if len(p) >= 3 and p == p[::-1]}