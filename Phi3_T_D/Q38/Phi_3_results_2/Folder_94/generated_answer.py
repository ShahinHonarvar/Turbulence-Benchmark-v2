import math

def find_subset_of_length_n(elements):
    n = 93
    if len(elements) < n:
        return 0
    elif len(elements) == n:
        return 1
    else:
        return math.comb(len(elements), n)