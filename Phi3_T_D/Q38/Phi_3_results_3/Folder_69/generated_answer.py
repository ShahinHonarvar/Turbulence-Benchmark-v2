from math import comb

def find_subset_of_length_n(elements):
    n = 894
    num_elements = len(elements)
    if n > num_elements:
        return 0
    return comb(num_elements, n)