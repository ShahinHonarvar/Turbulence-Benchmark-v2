def find_subset_of_length_n(elements):
    n = 64
    return len({frozenset(s) for i in range(len(elements) + 1) for s in combinations(elements, i) if len(s) == n})