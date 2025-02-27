def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=ord)
    smallest_90 = sorted_chars[:90]
    return sorted(smallest_90, key=ord, reverse=True)