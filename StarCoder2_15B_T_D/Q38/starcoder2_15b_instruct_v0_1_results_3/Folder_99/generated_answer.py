import math

def find_subset_of_length_n(elements):
    n = len(elements)
    k = 307
    return math.comb(n, k)