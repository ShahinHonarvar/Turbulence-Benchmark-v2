def return_n_smallest_chars(s):
    if len(s) > 64:
        s = sorted(s)[:64]
    return s[::-1]