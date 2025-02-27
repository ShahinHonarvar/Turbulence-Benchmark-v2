from itertools import combinations

def find_subset_of_length_n(elements):
    length = 16
    return len(list(combinations(elements, length)))