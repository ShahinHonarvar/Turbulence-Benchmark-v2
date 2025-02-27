from math import comb

def find_subset_of_length_n(elements):
    total_elements = len(elements)
    subset_size = 86
    if total_elements < subset_size:
        return 0
    return comb(total_elements, subset_size)