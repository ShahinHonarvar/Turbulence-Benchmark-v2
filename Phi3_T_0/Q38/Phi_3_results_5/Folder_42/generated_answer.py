def find_subset_of_length_n(elements):
    n = 31
    return sum((1 for subset in combinations(elements, n)))