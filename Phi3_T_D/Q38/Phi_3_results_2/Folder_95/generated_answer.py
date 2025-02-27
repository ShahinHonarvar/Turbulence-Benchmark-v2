from math import comb

def find_subset_of_length_n(elements):
    n = 87
    total_subsets = comb(len(elements), n)
    return total_subsets