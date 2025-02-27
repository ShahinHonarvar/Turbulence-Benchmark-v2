def find_subset_of_length_n(elements):
    n = 66
    count = 0
    for subset in itertools.combinations(elements, n):
        count += 1
    return count