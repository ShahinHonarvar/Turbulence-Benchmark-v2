def find_subset_of_length_n(elements):
    n = 40
    if len(elements) < n:
        return 0
    return len(elements) - n + 1