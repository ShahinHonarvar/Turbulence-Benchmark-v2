from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:6]
    letters = [char for char in substring if char.isalpha()]
    if len(letters) < 4:
        return set()
    perms = set([''.join(p) for p in permutations(letters, 4)])
    palindromes = {word.lower() for word in perms if word.lower() == word.lower()[::-1]}
    return palindromes