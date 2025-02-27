def find_subset_of_length_n(elements_set):
    total_subsets = 0
    for subset in itertools.combinations(elements_set, 17):
        total_subsets += 1
    return total_subsets