def find_subset_of_length_n(set_of_elements):
    n = len(set_of_elements)
    r = 72
    num_combinations = factorial(n) // (factorial(r) * factorial(n - r))
    return num_combinations