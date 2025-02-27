def find_subset_of_length_n(elements):
    n = 56
    return sum((1 for subset in itertools.combinations(elements, n)))