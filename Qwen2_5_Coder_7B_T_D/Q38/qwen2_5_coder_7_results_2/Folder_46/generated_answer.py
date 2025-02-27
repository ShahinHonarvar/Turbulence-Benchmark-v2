def find_subset_of_length_n(elements):
    n = 14
    return len(list(itertools.combinations(elements, n)))