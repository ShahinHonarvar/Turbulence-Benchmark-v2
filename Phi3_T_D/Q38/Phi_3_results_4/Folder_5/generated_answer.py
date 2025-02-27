from math import comb

def find_subset_of_length_n(elements):
    n = 67
    return comb(len(elements), n)