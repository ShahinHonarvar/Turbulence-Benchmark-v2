def return_n_smallest_chars(string):
    sorted_chars = sorted(string)
    n_smallest_chars = sorted_chars[:76][::-1]
    return n_smallest_chars