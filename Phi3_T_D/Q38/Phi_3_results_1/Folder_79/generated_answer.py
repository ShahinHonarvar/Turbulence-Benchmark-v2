def find_subset_of_length_n(elements):
    total_subsets = 1
    for _ in range(63):
        total_subsets *= len(elements)
    total_subsets //= 63 * math.factorial(63)
    return total_subsets