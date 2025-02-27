from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[4:8])).lower()
    p = set((''.join(i) for i in permutations(letters, len(letters))))
    return {x for x in p if len(x) >= 4 and x == x[::-1]}