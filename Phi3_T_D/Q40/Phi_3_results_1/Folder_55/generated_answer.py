def return_n_smallest_chars(s):
    smallest_chars = sorted(list(s))[:75]
    smallest_chars.reverse()
    return smallest_chars