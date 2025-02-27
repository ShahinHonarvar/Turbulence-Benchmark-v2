def return_n_smallest_chars(s):
    sorted_chars = sorted(s)
    n = min(17, len(sorted_chars))
    return sorted_chars[:n]