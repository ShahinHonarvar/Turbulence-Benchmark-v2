def find_subset_of_length_n(elements):
    n = 219
    all_subsets = [set(subset) for subset in itertools.combinations(elements, n)]
    return len(all_subsets)