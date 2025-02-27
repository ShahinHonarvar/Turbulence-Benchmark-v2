from math import comb

def find_subset_of_length_n(elements):
    n = len(elements)
    if n < 84:
        return 0
    return comb(n, 84)