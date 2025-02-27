def find_subset_of_length_n(s):
    n = len(s)
    subset_size = 630
    if n < subset_size:
        return 0
    total_subsets = 1
    for i in range(n, n - subset_size, -1):
        total_subsets *= i
    for i in range(1, subset_size + 1):
        total_subsets //= i
    return total_subsets