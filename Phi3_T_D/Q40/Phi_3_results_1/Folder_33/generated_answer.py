def return_n_smallest_chars(chars):
    smallest_chars = sorted(chars, reverse=True)[:36]
    return smallest_chars