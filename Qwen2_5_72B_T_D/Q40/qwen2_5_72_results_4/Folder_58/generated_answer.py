def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=ord)
    smallest_49 = sorted_chars[:49]
    return sorted(smallest_49, key=ord, reverse=True)