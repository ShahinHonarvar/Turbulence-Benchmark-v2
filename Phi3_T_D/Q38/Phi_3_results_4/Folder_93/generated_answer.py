from itertools import combinations

def find_subset_of_length_n(elements):
    subset_count = len(list(combinations(elements, 45)))
    return subset_count