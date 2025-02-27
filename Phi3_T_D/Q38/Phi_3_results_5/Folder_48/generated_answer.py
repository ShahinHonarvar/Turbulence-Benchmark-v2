from itertools import combinations

def find_subset_of_length_n(elements):
    target_subset_count = combinations(elements, 793)
    return sum((1 for _ in target_subset_count))