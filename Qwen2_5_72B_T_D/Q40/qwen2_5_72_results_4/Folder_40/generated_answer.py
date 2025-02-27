def return_n_smallest_chars(s):
    smallest_chars = sorted(s)[:7]
    return sorted(smallest_chars, reverse=True)