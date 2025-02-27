from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:9].lower()
    all_permutations = {''.join(p) for p in permutations(substring)}
    palindromes = {word for word in all_permutations if word == word[::-1] and len(word) >= 7}
    return palindromes