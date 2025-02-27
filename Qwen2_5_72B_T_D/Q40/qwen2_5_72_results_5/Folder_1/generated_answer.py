def return_n_smallest_chars(s):
    s_sorted = sorted(s)
    smallest_chars = s_sorted[:11]
    return sorted(smallest_chars, reverse=True)