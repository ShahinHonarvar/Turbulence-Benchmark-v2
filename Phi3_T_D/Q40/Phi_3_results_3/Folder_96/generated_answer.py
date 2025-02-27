def return_n_smallest_chars(s):
    chars = sorted(s)
    return sorted(chars, reverse=True)[:20]