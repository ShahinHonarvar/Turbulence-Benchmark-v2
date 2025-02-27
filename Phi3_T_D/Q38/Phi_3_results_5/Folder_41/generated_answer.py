from math import comb

def find_subset_of_length_n(elements):
    n = 84
    elements_count = len(elements)
    if elements_count >= n:
        return comb(elements_count, n)
    else:
        return 0