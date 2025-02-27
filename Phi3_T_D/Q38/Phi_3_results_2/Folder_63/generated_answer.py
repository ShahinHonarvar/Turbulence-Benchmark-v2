def find_subset_of_length_n(elements):
    n = len(elements)
    return 0 if n < 57 else comb(n, 57)