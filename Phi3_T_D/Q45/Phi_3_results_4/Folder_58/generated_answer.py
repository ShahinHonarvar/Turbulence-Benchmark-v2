import itertools

def palindromes_between_indices(s):
    indices = s[:7].lower()
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    found_letters = ''.join(sorted(set(indices) & set(english_letters)))
    combinations = set((''.join(perm) for perm in itertools.permutations(found_letters * 3, 3)))
    return set((comb for comb in combinations if comb == comb[::-1]))