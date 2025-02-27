from itertools import combinations

def find_subset_of_length_n(elements, n=24):
    return len(list(combinations(elements, n)))