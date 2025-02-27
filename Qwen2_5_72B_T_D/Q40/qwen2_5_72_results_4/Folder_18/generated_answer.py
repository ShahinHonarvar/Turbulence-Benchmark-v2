def return_n_smallest_chars(s):
    smallest_chars = sorted(list(s))[:52]
    return sorted(smallest_chars, reverse=True)