def return_n_smallest_chars(s):
    l = sorted(s)[:59]
    l.sort(reverse=True)
    return l