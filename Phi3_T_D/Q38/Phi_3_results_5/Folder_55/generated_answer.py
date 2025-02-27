def find_subset_of_length_n(elements):
    n = 21
    return int(sum((1 for subset in itertools.combinations(elements, n))))