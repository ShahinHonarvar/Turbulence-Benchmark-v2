from math import comb

def find_subset_of_length_n(elements):
    count = 0
    n = len(elements)
    if n < 64:
        return 0
    else:
        count = comb(n, 64)
    return count