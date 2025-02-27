import math

def find_subset_of_length_n(elements):
    n = len(elements)
    subset_count = math.comb(n, 99)
    return subset_count