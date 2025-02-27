def find_subset_of_length_n(elements_set):
    return len({frozenset(subset) for subset in combinations(elements_set, 449)})