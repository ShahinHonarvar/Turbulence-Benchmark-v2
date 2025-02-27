from math import comb

def find_subset_of_length_n(elements):
    n = len(elements)
    return comb(n, 372) if n >= 372 else 0