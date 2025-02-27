from itertools import combinations

def find_subset_of_length_n(elements_set):
    if len(elements_set) < 21:
        return 0
    return len(list(combinations(elements_set, 21)))