def find_subset_of_length_n(elements):
    num_elements = len(elements)
    return int(num_elements * (num_elements - 1) * (num_elements - 2) * (num_elements - 3) * (num_elements - 4) * (num_elements - 5) * (num_elements - 6) * (num_elements - 7) / (8 * 7 * 6 * 5 * 4 * 3 * 2 * 1))