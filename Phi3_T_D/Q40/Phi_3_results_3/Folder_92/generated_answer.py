def return_n_smallest_chars(chars):
    chars_sorted = sorted(chars)
    n_smallest_chars = chars_sorted[:63]
    return n_smallest_chars