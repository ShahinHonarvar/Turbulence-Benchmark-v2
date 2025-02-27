def return_n_smallest_chars(s):
    n = 64
    return sorted(sorted(s), reverse=True)[:n]