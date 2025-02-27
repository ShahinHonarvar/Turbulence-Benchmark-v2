from math import comb

def find_subset_of_length_n(elements):
    n = 872
    return comb(len(elements), n) if len(elements) >= n else 0