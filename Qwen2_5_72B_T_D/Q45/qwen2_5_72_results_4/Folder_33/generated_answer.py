from itertools import permutations

def palindromes_between_indices(s):
    substring = s[7:10]
    all_perms = set([''.join(p) for p in permutations(substring)])
    palindromes = {word.lower() for word in all_perms if len(word) >= 4 and word.lower() == word[::-1].lower()}
    return palindromes