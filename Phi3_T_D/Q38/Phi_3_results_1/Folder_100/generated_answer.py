def find_subset_of_length_n(elements):
    return len({el for subset in itertools.combinations(elements, 99) for el in subset})