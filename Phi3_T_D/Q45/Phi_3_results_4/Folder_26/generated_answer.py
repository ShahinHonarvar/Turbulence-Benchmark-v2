from itertools import permutations

def palindromes_between_indices(s):
    letters = sorted(set(s[4:7].lower()))
    palindromes = {''.join(p) for i in range(3, 7) for p in permutations(letters, i)}
    return {p for p in palindromes if p == p[::-1]}