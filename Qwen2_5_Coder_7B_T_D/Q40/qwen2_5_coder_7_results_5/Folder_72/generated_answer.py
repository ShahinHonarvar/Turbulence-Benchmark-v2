def return_n_smallest_chars(s):
    n = 37
    smallest_chars = sorted(s)[:n]
    sorted_chars = sorted(smallest_chars, reverse=True)
    return sorted_chars