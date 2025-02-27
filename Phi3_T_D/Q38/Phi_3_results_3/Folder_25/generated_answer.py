import math

def find_subset_of_length_n(elements):
    n = 90
    count = 0
    num_elements = len(elements)
    if n > num_elements:
        return 0
    return 1 if n == 0 else math.comb(num_elements, n)