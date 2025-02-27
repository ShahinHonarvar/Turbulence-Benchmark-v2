def find_subset_of_length_n(elements):
    n = len(elements)
    k = 4
    if n < k:
        return 0
    return n * (n - 1) * (n - 2) * (n - 3) // math.factorial(4)