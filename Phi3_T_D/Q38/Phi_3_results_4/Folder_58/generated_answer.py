from itertools import combinations

def find_subset_of_length_n(elements):
    n = 860
    subsets = list(combinations(elements, n))
    return len(subsets)