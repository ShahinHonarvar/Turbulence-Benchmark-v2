def return_n_smallest_chars(chars_string):
    smallest_chars = sorted(chars_string)
    return smallest_chars[:min(63, len(smallest_chars))]