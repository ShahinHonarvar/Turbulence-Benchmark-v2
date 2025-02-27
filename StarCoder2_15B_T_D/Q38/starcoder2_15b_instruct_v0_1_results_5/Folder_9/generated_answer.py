def find_subset_of_length_n(elements):
    n = 24
    return len(elements) >= n and sum((1 for _ in elements)) == n