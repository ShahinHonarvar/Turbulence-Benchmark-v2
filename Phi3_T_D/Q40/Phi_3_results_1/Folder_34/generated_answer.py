def return_n_smallest_chars(s):
    smallest_chars = sorted(set(s))[:9]
    return sorted(smallest_chars, reverse=True)