from math import comb

def find_subset_of_length_n(element_set):
    n = len(element_set)
    if n < 307:
        return 0
    return comb(n, 307)