from itertools import permutations

def palindromes_between_indices(s):
    substring = s[5:7].lower()
    all_perms = {''.join(p) for p in permutations(substring)}
    all_palindromes = {word for word in all_perms if len(word) >= 3 and word == word[::-1]}
    return all_palindromes