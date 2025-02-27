def return_n_smallest_chars(s):
    return sorted(s, reverse=True, key=ord)[:75]