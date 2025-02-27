def find_subset_of_length_n(elements_set):
    n = 49
    count = 0
    for subset in itertools.combinations(elements_set, n):
        count += 1
    return count