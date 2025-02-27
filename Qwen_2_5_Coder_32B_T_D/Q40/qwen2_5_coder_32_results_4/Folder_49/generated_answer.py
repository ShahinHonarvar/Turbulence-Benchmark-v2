def return_n_smallest_chars(s):
    t = sorted(s)[:76]
    return sorted(t, reverse=True)