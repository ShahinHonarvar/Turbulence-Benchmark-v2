def return_n_smallest_chars(chars):
    smallest_chars = sorted(list(chars))[:66]
    smallest_chars.reverse()
    return smallest_chars