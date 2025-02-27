def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=ord)
    smallest_26 = sorted_chars[:26]
    return sorted(smallest_26, key=ord, reverse=True)