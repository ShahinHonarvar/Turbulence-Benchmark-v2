from itertools import combinations

def find_subset_of_length_n(elements_set):
    n = 793
    return len(list(combinations(elements_set, n)))