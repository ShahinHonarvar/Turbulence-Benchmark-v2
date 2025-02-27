from math import comb

def find_subset_of_length_n(elements):
    return comb(len(elements), 97) if len(elements) >= 97 else 0