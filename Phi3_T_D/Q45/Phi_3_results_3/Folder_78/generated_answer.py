from itertools import permutations

def palindromes_between_indices(s):
    substring = s[6:10]
    substring = substring.lower()
    letters = ''.join(filter(str.isalpha, substring))
    perms = {''.join(p) for i in range(3, len(letters) + 1) for p in permutations(letters, i)}
    palindromes = {perm for perm in perms if perm == perm[::-1]}
    return palindromes