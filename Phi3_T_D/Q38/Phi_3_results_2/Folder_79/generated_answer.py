from itertools import combinations

def find_subset_of_length_n(elements):
    subset_count = 0
    subset_length = 63
    subset_length_combinations = combinations(elements, subset_length)
    for _ in subset_length_combinations:
        subset_count += 1
    return subset_count