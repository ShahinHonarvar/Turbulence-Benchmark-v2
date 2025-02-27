from math import comb

def find_subset_of_length_n(elements_set):
    N = len(elements_set)
    return comb(N, 27)