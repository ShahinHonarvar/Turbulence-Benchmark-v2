from itertools import combinations

def find_subset_of_length_n(elements):
    desired_subset_size = 89
    return len(list(combinations(elements, desired_subset_size)))