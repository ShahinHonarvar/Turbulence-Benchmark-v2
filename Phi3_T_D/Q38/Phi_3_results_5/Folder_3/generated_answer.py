import math
        from itertools import combinations

def find_subset_of_length_n(element_set):
    if len(element_set) < 100:
        return 0
    else:
        return math.comb(len(element_set), 100)