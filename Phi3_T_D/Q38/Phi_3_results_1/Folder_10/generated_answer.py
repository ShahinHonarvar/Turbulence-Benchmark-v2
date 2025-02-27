from itertools import combinations

def find_subset_of_length_n(elements):
    target_length = 54
    return len(list(combinations(elements, target_length)))