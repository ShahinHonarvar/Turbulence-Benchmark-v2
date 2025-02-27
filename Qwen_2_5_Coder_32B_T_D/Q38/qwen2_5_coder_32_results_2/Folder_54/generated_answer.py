import math

def find_subset_of_length_n(s):
    n = len(s)
    return math.comb(n, 51) if n >= 51 else 0