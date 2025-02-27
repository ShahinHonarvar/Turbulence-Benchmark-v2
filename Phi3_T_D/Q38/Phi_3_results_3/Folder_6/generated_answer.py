from itertools import combinations

def find_subset_of_length_n(elements):
    n = 89
    return len(list(combinations(elements, n)))