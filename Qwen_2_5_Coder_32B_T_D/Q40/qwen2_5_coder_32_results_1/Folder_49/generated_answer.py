def return_n_smallest_chars(s):
    t = sorted(list(s))[:76]
    return t[::-1]