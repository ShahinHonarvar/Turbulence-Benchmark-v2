def find_subset_of_length_n(elements_set):
    n = 93
    return sum((1 for i in range(len(elements_set) + 1) for subset in combinations(elements_set, i) if len(subset) == n))