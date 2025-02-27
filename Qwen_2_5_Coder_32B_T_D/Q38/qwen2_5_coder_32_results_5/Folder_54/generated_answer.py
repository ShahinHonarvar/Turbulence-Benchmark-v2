from math import comb

def find_subset_of_length_n(elements):
    return comb(len(elements), 51) if 51 <= len(elements) else 0