def find_subset_of_length_n(elements_set):
    return len([subset for subset in elements_set if len(subset) == 1])