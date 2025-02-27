from itertools import permutations

def palindromes_between_indices(s):
    indices = range(2, 9)
    substr = s[2:9].lower()
    chars = ''.join(sorted(set(substr), key=substr.index))
    possible_combinations = set((''.join(p) for p in permutations(chars, 6)))
    palindromes = {comb for comb in possible_combinations if comb == comb[::-1]}
    return palindromes