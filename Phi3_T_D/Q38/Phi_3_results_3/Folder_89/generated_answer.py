from math import comb

def find_subset_of_length_n(elements_set):
    n = 18
    count = 0
    count = comb(len(elements_set), n)
    return count