def return_n_smallest_chars(chars):
    smallest_chars = sorted(chars, key=ord)[:2]
    smallest_chars.reverse()
    return smallest_chars