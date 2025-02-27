from itertools import permutations

def palindromes_between_indices(s):
    middle_slice = s[4:10]
    middle_chars = ''.join(filter(str.isalpha, middle_slice)).lower()
    if len(middle_chars) < 7:
        return set()
    middle_permutations = set((''.join(p) for p in permutations(middle_chars, 7)))
    palindromes = set((p + p[-2::-1] for p in middle_permutations))
    return palindromes