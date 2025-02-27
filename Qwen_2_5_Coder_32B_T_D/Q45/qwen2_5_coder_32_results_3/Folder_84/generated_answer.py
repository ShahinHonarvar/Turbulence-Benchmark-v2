from itertools import permutations

def palindromes_between_indices(s):
    chars = [c.lower() for c in s[4:10] if c.isalpha()]
    perms = set((''.join(p) for p in permutations(chars)))
    palindromes = {word for word in perms if len(word) >= 3 and word == word[::-1]}
    return palindromes