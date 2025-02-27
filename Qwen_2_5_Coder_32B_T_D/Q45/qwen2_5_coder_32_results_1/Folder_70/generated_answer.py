from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:7] if c.isalpha()]
    perms = set((''.join(p) for p in permutations(letters)))
    palindromes = {word for word in perms if len(word) >= 4 and word == word[::-1]}
    return palindromes