from itertools import combinations

def all_substring_of_size_n(s):
    return [''.join(comb) for comb in combinations(set(s), 84) if len(set(comb)) == 84]