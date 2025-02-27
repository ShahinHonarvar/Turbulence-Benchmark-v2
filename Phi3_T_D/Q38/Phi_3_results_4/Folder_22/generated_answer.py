from math import comb

def find_subset_of_length_n(s):
    n = 72
    return comb(len(s), n)