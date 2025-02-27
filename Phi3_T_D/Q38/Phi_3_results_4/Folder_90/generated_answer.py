def find_subset_of_length_n(s):
    n = 752
    return sum((1 for subset in combinations(s, n) if len(subset) == n))