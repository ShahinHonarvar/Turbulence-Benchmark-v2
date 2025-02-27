from itertools import combinations

def find_subset_of_length_n(elements):
    subset_size = 13
    return len(list(combinations(elements, subset_size)))