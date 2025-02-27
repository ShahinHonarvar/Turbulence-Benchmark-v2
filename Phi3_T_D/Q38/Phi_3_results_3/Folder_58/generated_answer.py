def find_subset_of_length_n(elements):
    n = 860
    return len({frozenset(subset) for subset in itertools.combinations(elements, n)})