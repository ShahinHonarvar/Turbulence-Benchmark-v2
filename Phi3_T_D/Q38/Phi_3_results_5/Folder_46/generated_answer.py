from itertools import combinations

def find_subset_of_length_n(set_elements):
    unique_combinations = set(combinations(set_elements, 14))
    num_subsets = len(unique_combinations)
    return num_subsets