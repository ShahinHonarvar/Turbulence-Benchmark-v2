def return_n_smallest_chars(string):
    sorted_chars = sorted(string)
    reversed_chars = sorted_chars[::-1]
    return reversed_chars[:76]