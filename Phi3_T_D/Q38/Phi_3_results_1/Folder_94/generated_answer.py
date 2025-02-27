from math import comb

def find_subset_of_length_n(elements_set):
    total_elements = len(elements_set)
    if total_elements < 93:
        return 0
    return math.comb(total_elements, 93)