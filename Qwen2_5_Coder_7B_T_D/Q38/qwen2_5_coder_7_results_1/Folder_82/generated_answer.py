def find_subset_of_length_n(elements):
    n = 83
    if len(elements) < n:
        return 0
    return len(list(itertools.combinations(elements, n)))