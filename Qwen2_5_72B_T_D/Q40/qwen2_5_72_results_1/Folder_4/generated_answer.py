def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=ord)
    smallest_n_chars = sorted_chars[:90]
    return sorted(smallest_n_chars, key=ord, reverse=True)