def find_subset_of_length_n(elements_set):
    n = 722
    subset_count = 1
    for _ in range(n):
        subset_count *= len(elements_set)
        elements_set = elements_set.difference(elements_set)
    return subset_count - 1