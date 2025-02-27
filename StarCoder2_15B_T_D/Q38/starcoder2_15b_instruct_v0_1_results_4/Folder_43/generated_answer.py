def find_subset_of_length_n(set_of_elements):
    n = 29
    num_subsets = 0
    for i in range(len(set_of_elements) - n + 1):
        subset = set_of_elements[i:i + n]
        num_subsets += 1
    return num_subsets