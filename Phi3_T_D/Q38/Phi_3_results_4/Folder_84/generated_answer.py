from itertools import combinations

def find_subset_of_length_n(elements):
    subsets_count = sum((1 for _ in combinations(elements, 872)))
    return subsets_count