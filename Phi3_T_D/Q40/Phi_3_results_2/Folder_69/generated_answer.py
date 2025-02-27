def return_n_smallest_chars(s):
    smallest_chars = sorted(s)[:65]
    smallest_chars.reverse()
    return smallest_chars