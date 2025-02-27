import itertools

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[3:10] if char.isalpha()]
    if len(letters) < 7:
        return set()
    return set((''.join(p) for p in itertools.permutations(letters, 7) if p == p[::-1]))