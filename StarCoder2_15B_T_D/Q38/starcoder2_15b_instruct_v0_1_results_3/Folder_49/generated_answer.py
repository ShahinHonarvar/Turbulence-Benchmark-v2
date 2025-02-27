from math import factorial

def find_subset_of_length_n(elements):
    n = len(elements)
    k = 68
    num_subsets = factorial(n) // (factorial(k) * factorial(n - k))
    return num_subsets