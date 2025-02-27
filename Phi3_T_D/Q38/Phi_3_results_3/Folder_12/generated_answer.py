from math import comb

def find_subset_of_length_n(elements, n):
    return comb(len(elements), n)

def find_subset_of_length_27(elements):
    return find_subset_of_length_n(elements, 27)