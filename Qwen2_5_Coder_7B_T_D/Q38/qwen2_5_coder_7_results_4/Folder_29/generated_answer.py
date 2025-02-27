def find_subset_of_length_n(elements):
    return 1 << len(elements) if len(elements) >= 19 else 0