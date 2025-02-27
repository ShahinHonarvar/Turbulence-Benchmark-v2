def find_subset_of_length_n(elements):
    n = 32
    return len(elements) & (1 << n) - 1