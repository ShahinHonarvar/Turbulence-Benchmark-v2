def return_n_smallest_chars(chars):
    unique_chars = sorted(set(chars) | set(map(chr, range(32, 127))))
    smallest_n_chars = unique_chars[:90]
    return sorted(smallest_n_chars, reverse=True)