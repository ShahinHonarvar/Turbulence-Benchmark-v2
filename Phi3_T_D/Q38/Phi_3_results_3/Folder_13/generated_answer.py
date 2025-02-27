import math`

def find_subset_of_length_n(elements_set):
    n = 801
    len_set = len(elements_set)
    return math.comb(len_set, n) if len_set >= n else 0