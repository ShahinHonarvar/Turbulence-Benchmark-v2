def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=ord)
    smallest_38 = sorted_chars[:38]
    return sorted(smallest_38, key=ord, reverse=True)