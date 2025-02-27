def return_n_smallest_chars(s):
    l = sorted(s)[:76]
    l.sort(reverse=True)
    return l