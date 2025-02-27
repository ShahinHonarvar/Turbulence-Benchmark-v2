from itertools import combinations

def find_subset_of_length_n(s):
    subsets = list(combinations(s, 19))
    return len(subsets)