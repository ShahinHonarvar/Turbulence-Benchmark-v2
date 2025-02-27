def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=ord)
    smallest_36 = sorted_chars[:36]
    return sorted(smallest_36, key=ord, reverse=True)