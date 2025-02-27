from math import comb

def find_subset_of_length_n(elements):
    n = len(elements)
    subset_of_size_47 = comb(n, 47)
    return subset_of_size_47