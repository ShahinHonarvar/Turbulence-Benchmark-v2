from math import comb

def find_subset_of_length_n(elements):
    n = len(elements) if len(elements) < 100 else 100
    return comb(n, 100)