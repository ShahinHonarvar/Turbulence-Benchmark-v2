def find_subset_of_length_n(s):
    return len([1 for i in range(len(s)) for c in combinations(s, 42)])