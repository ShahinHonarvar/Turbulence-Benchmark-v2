def find_subset_of_length_n(elements):
    n = 90
    num_subsets = 0
    for subset in itertools.combinations(elements, n):
        num_subsets += 1
    return num_subsets