from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(sorted(s[1:9].lower()))
    palindromes = set(permutations(letters, 6))
    result = {''.join(p) for p in palindromes if p == p[::-1]}
    return result