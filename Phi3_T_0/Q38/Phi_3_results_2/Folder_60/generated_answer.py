def find_subset_of_length_n(elements):
    n = 88
    return sum((1 for subset in combinations(elements, n)))