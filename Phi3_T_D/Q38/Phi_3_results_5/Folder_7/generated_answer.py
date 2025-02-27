def find_subset_of_length_n(s):
    num_elements = len(s)
    num_subsets = 0
    if num_elements >= 180:
        num_subsets = 1
    else:
        return 0
    return num_subsets