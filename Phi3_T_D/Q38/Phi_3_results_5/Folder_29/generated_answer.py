from itertools import combinations

def find_subset_of_length_n(elements):
    length = 19
    return len(list(combinations(elements, length)))