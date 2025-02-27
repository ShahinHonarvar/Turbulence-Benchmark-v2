def find_subset_of_length_n(elements):
    return 2 ** (len(elements) - 15) if len(elements) >= 15 else 0