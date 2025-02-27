from itertools import permutations

def palindromes_between_indices(s):
    s = s[:7].lower()
    letters = ''.join(filter(str.isalpha, s))
    permutations_set = set((''.join(p) for i in range(3, len(letters) + 1) for p in permutations(letters, i)))
    return {p for p in permutations_set if p == p[::-1]}