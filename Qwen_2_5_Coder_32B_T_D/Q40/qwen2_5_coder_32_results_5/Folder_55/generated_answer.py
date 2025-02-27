def return_n_smallest_chars(s):
    n = min(75, len(s))
    smallest_chars = sorted(s)[:n]
    return sorted(smallest_chars, reverse=True)