def return_n_smallest_chars(s):
    a = sorted(s)[:2]
    a.sort(reverse=True)
    return a