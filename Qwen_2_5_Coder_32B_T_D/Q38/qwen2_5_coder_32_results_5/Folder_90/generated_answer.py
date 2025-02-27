from math import comb

def find_subset_of_length_n(s):
    return comb(len(s), 752) if len(s) >= 752 else 0