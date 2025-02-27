def find_subset_of_length_n(elements):
    if len(elements) < 2:
        return 0
    else:
        return len(elements) * (len(elements) - 1) // 2