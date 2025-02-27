def find_subset_of_length_n(elements):
    n = 97
    return len({frozenset(subset) for subset in combinations(elements, n)})