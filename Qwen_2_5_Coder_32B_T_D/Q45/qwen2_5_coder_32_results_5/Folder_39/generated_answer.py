from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:6].lower()
    letters = ''.join([c for c in s if c.isalpha()])
    perms = set((''.join(p) for p in permutations(letters, len(letters))))
    palindromes = {word for word in perms if len(word) >= 3 and word == word[::-1]}
    return palindromes