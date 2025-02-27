from itertools import permutations

def palindromes_between_indices(s):
    substring = s[6:10].lower()
    all_perms = {''.join(p) for p in permutations(substring)}
    palindromes = {word for word in all_perms if word == word[::-1] and len(word) >= 4}
    return palindromes