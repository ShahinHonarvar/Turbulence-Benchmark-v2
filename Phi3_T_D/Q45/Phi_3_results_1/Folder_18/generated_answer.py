from itertools import permutations

def palindromes_between_indices(s):
    segment = s[1:7].lower()
    segments_set = set(segment)
    palindromes = set([''.join(p) for p in permutations(segment) if len(p) in [3, 5, 6] and p == p[::-1]])
    return palindromes