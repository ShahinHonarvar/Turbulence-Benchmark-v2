from math import comb, factorial

def find_subset_of_length_n(elements):
    len_elements = len(elements)
    if len_elements < 29:
        return 0
    return comb(len_elements, 29)