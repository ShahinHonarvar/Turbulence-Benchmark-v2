def find_subset_of_length_n(elements):
    count = 0
    n = 3
    for subset in itertools.combinations(elements, n):
        count += 1
    return count