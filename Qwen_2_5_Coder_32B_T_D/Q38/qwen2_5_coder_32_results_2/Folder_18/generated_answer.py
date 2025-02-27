from math import comb

def find_subset_of_length_n(s):
    return comb(len(s), 630) if len(s) >= 630 else 0