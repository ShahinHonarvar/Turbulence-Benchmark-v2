from itertools import combinations

def find_subset_of_length_n(E):
    if len(E) < 6:
        return 0
    return len(list(combinations(E, 6)))