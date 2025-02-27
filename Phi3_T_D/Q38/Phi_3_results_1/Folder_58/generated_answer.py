from itertools import combinations

def find_subset_of_length_n(elements):
    subset_count = sum((1 for subset in combinations(elements, 860)))
    return subset_count