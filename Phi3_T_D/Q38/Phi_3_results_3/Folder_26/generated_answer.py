def find_subset_of_length_n(elements):
    count = 0
    n = 25
    return sum((1 for _ in itertools.combinations(elements, n)))