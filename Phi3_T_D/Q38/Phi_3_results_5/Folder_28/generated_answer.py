from itertools import combinations

def find_subset_of_length_n(elements_set):
    n = 37
    if n > len(elements_set):
        return 0
    return len(list(combinations(elements_set, n)))