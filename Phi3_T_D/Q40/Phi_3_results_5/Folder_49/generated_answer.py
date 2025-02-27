def return_n_smallest_chars(s):
    smallest_chars = sorted(s)
    return sorted(smallest_chars, reverse=True)[:76]