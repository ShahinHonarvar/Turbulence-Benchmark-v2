def return_n_smallest_chars(string):
    sorted_chars = sorted(string)
    return list(reversed(sorted_chars[:49]))