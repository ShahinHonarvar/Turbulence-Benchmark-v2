from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:7]]
    unique_letters = ''.join(set(letters))
    length = len(unique_letters)
    if length < 3:
        return set()
    return set((''.join(p) for p in permutations(unique_letters) if p[0].islower()))