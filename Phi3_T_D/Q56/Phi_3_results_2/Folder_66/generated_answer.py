from itertools import combinations

def all_substring_of_size_n(s):
    return list(set([''.join(sub) for sub in combinations(set(s), 26) if len(s) >= 26]))