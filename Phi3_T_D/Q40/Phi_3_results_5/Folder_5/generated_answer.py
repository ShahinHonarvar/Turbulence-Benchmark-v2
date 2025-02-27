def return_n_smallest_chars(s):
    n = min(46, len(s))
    sorted_chars = sorted(s, key=ord)[:n]
    return sorted_chars[::-1]