def return_n_smallest_chars(s):
    n = 61
    chars = sorted(s)
    return chars[-n:][::-1]