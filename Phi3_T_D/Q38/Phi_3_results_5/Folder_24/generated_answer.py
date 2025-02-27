def find_subset_of_length_n(elements_set):
    n = 74
    return sum((1 for subset in itertools.combinations(elements_set, n)))