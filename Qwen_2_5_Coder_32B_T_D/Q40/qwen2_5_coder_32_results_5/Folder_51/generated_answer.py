def return_n_smallest_chars(s):
    l = sorted(list(s))[:45]
    return sorted(l, reverse=True)