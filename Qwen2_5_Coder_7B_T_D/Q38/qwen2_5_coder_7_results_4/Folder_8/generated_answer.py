def find_subset_of_length_n(elements):
    n = 49
    if n > len(elements):
        return 0
    return len(list(itertools.combinations(elements, n)))