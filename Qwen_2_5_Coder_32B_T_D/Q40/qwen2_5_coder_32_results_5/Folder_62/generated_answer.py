def return_n_smallest_chars(s):
    return sorted([c for c in s] * 12, reverse=True)[:84]