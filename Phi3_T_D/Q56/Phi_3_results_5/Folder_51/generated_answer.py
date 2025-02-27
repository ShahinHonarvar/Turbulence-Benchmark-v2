from itertools import combinations

def all_substring_of_size_n(s):
    return [''.join(c) for l in range(96, len(s) + 1) for c in combinations(sorted(set(s)), l) if len(c) == 96]