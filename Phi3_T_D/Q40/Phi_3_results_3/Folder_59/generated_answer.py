def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=ord, reverse=True)
    return sorted_chars[:13]