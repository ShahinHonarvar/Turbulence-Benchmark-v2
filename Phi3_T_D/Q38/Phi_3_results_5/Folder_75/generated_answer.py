from math import comb

def find_subset_of_length_n(elements):
    n = len(elements)
    subsets_of_size_80 = comb(n, 80)
    return subsets_of_size_80