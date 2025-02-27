def find_subset_of_length_n(set_of_elements):
    num_elements = len(set_of_elements)
    num_subsets = num_elements * (num_elements - 1) // 2
    return num_subsets