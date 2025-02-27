from math import comb

def find_subset_of_length_n(set_elements):
    n = 28
    return comb(len(set_elements), n)