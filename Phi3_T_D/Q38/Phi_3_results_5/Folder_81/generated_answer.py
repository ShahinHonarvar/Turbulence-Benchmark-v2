from itertools import combinations

def find_subset_of_length_n(elements, n=20):
    return len(list(combinations(elements, n)))