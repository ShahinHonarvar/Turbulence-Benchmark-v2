def return_n_smallest_chars(s):
    l = sorted(s)[:49]
    l.sort(reverse=True)
    return l