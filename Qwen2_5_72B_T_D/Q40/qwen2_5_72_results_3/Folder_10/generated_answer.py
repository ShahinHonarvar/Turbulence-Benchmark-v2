def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=ord)
    smallest_88 = sorted_chars[:88]
    return sorted(smallest_88, key=ord, reverse=True)