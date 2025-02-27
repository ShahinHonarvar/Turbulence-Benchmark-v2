def return_n_smallest_chars(s):
    unique_chars = sorted(list(set(s)), key=ord)
    return unique_chars[:36]