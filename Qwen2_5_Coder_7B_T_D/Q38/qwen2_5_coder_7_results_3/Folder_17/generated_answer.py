def find_subset_of_length_n(elements):
    n = 76
    return len(list(itertools.combinations(elements, n)))