def find_subset_of_length_n(elements):
    n = 534
    subset_count = 1
    for i in range(n):
        subset_count *= (len(elements) - i) / (i + 1)
    return int(subset_count)