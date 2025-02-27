def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=ord)
    smallest_chars = sorted_chars[:28]
    return sorted(smallest_chars, key=ord, reverse=True)