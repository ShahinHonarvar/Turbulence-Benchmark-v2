def find_subset_of_length_n(set_of_elements):
    n = len(set_of_elements)
    k = 49
    num_subsets = factorial(n) / (factorial(k) * factorial(n - k))
    return num_subsets