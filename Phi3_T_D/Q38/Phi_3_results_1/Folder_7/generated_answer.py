from itertools import combinations

def find_subset_of_length_n(elements):
    subsets_count = len(list(combinations(elements, 180)))
    return subsets_count