from itertools import combinations

def find_subset_of_length_n(elements):
    k = 219
    return len(list(combinations(elements, k)))