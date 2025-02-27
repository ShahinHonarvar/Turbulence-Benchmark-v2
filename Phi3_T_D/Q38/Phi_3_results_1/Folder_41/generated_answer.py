from itertools import combinations

def find_subset_of_length_n(S):
    subsets = list(combinations(S, 84))
    return len(subsets)