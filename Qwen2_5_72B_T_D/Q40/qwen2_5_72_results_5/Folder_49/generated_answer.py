def return_n_smallest_chars(s):
    smallest_chars = sorted(list(s))[:76]
    return sorted(smallest_chars, reverse=True)