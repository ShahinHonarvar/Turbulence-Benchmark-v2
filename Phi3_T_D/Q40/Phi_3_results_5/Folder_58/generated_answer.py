def return_n_smallest_chars(chars):
    smallest_chars = sorted(chars)[:49]
    return sorted(smallest_chars, reverse=True)