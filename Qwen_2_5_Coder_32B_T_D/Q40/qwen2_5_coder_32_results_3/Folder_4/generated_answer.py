def return_n_smallest_chars(s):
    l = sorted(s)[:90]
    l.sort(reverse=True)
    return l