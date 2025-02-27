def find_subset_of_length_n(elements):
    n = len(elements)
    k = 1
    num_subsets = n * (n - 1) // 2
    return num_subsets