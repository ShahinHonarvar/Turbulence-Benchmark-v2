def find_subset_of_length_n(s):
    return len([1 for _ in itertools.combinations(s, 64)]) if len(s) >= 64 else 0