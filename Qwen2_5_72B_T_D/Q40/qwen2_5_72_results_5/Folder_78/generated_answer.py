def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=ord)
    smallest_43 = sorted_chars[:43]
    return sorted(smallest_43, key=ord, reverse=True)