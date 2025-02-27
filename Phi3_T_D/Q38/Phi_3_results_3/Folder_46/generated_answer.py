from itertools import combinations

def find_subset_of_length_n(elems):
    return sum((1 for _ in combinations(elems, 14)))