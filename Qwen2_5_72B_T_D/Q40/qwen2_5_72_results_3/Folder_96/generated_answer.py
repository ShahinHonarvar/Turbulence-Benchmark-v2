def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=ord)
    smallest_20 = sorted_chars[:20]
    return sorted(smallest_20, key=ord, reverse=True)