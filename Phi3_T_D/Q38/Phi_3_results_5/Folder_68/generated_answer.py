def find_subset_of_length_n(elements):
    n = len(elements)
    if n < 3:
        return 0
    return n * (n - 1) * (n - 2) // 6