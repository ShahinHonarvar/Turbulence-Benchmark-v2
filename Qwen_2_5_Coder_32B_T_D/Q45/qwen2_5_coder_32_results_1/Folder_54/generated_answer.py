from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:10] if c.isalpha()]
    seen = set()
    for p in permutations(letters, len(letters)):
        candidate = ''.join(p)
        if candidate == candidate[::-1] and len(candidate) >= 4:
            seen.add(candidate)
    return seen