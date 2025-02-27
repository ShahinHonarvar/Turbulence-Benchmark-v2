def find_subset_of_length_n(elements_set):
    target_length = 66
    return sum((1 for subset in itertools.combinations(elements_set, target_length)))