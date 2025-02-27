from math import comb

def find_subset_of_length_n(elements_set):
    elements_count = len(elements_set)
    if elements_count < 894:
        return 0
    return comb(elements_count, 894)