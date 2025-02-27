def return_n_smallest_chars(s):
    if len(s) > 46:
        s = sorted(s)[:46]
    else:
        s = sorted(s, reverse=True)
    return s