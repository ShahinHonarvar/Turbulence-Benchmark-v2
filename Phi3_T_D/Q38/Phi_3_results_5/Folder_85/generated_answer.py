from math import factorial as f

def find_subset_of_length_n(elements):
    n = 23
    num_elements = len(elements)
    if n > num_elements:
        return 0
    return comb(num_elements, n)

def comb(n, k):
    return f(n) // (f(k) * f(n - k))