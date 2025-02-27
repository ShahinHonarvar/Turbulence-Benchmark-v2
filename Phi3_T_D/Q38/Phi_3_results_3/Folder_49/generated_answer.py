from math import comb

def find_subset_of_length_n(elements):
    n = len(elements)
    if n < 68:
        return 0
    else:
        return comb(n, 68)