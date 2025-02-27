def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=ord)
    smallest_64 = sorted_chars[:64]
    return sorted(smallest_64, key=ord, reverse=True)