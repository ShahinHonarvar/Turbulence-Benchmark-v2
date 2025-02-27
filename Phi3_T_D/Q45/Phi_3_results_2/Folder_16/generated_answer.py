from itertools import permutations

def palindromes_between_indices(s):
    substring = s[6:10].lower()
    perms = set((''.join(p) for p in permutations(substring)))
    palindromes = {word for word in perms if len(word) >= 5 and word == word[::-1]}
    return palindromes