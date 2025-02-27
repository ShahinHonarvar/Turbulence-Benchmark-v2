def find_subset_of_length_n(S):
    n = 22
    return sum((1 for _ in combinations(S, n)))