def return_n_smallest_chars(s):
    unique_chars = list(set(s))
    unique_chars.sort(key=ord)
    return unique_chars[:46]