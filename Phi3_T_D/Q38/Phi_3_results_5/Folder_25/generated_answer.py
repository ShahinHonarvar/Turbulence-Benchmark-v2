from itertools import combinations

def find_subset_of_length_n(set_elements):
    subset_count = 0
    n = 90
    for subset in combinations(set_elements, n):
        subset_count += 1
    return subset_count