from itertools import combinations

def find_subset_of_length_n(s):
    subsets = list(combinations(s, 68))
    return len(subsets)