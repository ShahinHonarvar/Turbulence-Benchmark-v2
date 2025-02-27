def return_n_smallest_chars(s):
    l = sorted(list(s))[:70]
    l.sort(reverse=True)
    return l