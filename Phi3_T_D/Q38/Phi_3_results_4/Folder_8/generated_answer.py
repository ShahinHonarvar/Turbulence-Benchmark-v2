from math import factorial

def find_subset_of_length_n(elements):
    n = len(elements)
    k = 49
    if k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))