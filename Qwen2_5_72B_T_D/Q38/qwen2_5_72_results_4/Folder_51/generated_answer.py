from itertools import combinations

def find_subset_of_length_n(elements):
    subset_size = 64
    return len(list(combinations(elements, subset_size)))