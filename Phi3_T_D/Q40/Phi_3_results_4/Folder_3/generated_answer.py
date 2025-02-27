def return_n_smallest_chars(s):
    str_sorted = sorted(s)
    return sorted(str_sorted[:28], reverse=True)