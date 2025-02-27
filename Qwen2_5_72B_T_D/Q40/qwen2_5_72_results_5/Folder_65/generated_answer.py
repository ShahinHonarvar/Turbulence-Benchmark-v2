def return_n_smallest_chars(s):
    s = sorted(s, key=ord)[:27]
    return sorted(s, key=ord, reverse=True)