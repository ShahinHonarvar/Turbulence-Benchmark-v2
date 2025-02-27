from math import comb

def find_subset_of_length_n(elements):
    n = min(len(elements), 64)
    return comb(n, 64)