from math import comb

def find_subset_of_length_n(elements_set):
    size = 36
    return comb(len(elements_set), size)