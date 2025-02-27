def return_n_smallest_chars(s):
    n = 66
    sorted_chars = sorted(s)
    return sorted_chars[:n][::-1]