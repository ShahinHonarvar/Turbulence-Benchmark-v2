def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=ord)
    smallest_65 = sorted_chars[:65]
    return sorted(smallest_65, key=ord, reverse=True)