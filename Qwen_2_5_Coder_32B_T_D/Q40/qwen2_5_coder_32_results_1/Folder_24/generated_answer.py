def return_n_smallest_chars(s):
    l = sorted(s)[:32]
    return sorted(l, reverse=True)