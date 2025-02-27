from itertools import combinations

def find_subset_of_length_n(elements_set):
    subset_count = sum((1 for _ in combinations(elements_set, 872)))
    return subset_count