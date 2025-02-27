import math

def find_subset_of_length_n(elements):
    n = len(elements)
    subsets_count = math.comb(n, 872)
    return subsets_count