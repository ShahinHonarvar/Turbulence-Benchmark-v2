def find_subset_of_length_n(s):
    if len(s) < 327:
        return 0
    return sum((1 for c in itertools.combinations(s, 327)))