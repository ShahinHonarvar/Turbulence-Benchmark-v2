def return_n_smallest_chars(s):
    l = sorted(s)[:61]
    return sorted(l, reverse=True)