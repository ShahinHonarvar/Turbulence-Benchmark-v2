def return_n_smallest_chars(s):
    l = sorted(s)[:39]
    l.sort(reverse=True)
    return l