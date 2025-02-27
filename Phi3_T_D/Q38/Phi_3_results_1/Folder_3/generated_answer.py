from math import comb

def find_subset_of_length_n(elements):
    n = 100
    if len(elements) < n:
        return 0
    return comb(len(elements), n)