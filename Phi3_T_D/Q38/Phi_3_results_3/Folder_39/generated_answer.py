import math

def find_subset_of_length_n(elements):
    n = len(elements)
    k = 59
    subsets_count = math.comb(n, k)
    return subsets_count