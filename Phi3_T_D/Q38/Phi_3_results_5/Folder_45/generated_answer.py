def find_subset_of_length_n(elements):
    n = 33
    if len(elements) < n:
        return 0
    return sum((1 for subset in itertools.combinations(elements, n)))