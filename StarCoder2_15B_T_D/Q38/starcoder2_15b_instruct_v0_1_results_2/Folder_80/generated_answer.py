def find_subset_of_length_n(elements):
    n = len(elements)
    k = 36
    return factorial(n) // (factorial(k) * factorial(n - k))