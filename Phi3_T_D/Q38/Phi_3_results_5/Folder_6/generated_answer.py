def find_subset_of_length_n(s):
    n = 89
    total_subsets = 0
    for subset in itertools.combinations(s, n):
        total_subsets += 1
    return total_subsets