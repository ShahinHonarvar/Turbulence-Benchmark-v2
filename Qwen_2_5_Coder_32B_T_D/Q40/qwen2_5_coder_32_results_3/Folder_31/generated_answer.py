def return_n_smallest_chars(s):
    a = sorted(list(s))[:70]
    a.sort(reverse=True)
    return a