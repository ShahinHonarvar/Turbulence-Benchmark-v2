from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:7].lower()
    all_permutations = {''.join(p) for p in permutations(substring)}
    palindromes = {word for word in all_permutations if word == word[::-1] and len(word) >= 4}
    return palindromes