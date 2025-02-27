def return_n_smallest_chars(s):
    return sorted([min(s), sorted([c for c in s if c != min(s)])[0]])