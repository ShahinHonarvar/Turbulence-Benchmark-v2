def find_subset_of_length_n(elements):
    n = len(elements)
    if n < 47:
        return 0
    return math.comb(n, 47)