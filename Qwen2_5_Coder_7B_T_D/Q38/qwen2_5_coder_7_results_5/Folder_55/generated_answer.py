def find_subset_of_length_n(elements):
    n = 21
    return len(elements) >= n and math.comb(len(elements), n)