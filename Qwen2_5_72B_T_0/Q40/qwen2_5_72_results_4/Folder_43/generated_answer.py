def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=ord)
    smallest_56 = sorted_chars[:56]
    return sorted(smallest_56, key=ord, reverse=True)