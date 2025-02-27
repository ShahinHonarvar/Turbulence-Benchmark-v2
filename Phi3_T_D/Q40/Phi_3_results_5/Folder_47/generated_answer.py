def return_n_smallest_chars(chars):
    smallest_chars = sorted(chars, key=ord)[:21]
    return sorted(smallest_chars, reverse=True)