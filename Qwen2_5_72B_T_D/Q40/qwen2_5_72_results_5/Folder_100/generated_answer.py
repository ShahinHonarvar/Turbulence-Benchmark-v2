def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=ord)
    smallest_72 = sorted_chars[:72]
    return sorted(smallest_72, key=ord, reverse=True)