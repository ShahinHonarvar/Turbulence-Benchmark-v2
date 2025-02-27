def return_n_smallest_chars(s):
    if len(s) <= 31:
        return sorted(s)
    else:
        return sorted(s)[:31]