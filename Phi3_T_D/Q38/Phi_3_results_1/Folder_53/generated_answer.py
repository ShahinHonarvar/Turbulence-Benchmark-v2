from math import comb

def find_subset_of_length_n(s):
    n = len(s)
    if n < 73:
        return 0
    else:
        return comb(n, 73)