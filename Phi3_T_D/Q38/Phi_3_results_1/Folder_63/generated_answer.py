def find_subset_of_length_n(elements_set):
    n = 57
    num_elements = len(elements_set)
    if n > num_elements:
        return 0
    return 1 if num_elements == n else 0