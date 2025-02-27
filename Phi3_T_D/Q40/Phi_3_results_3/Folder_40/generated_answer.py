def return_n_smallest_chars(s):
    n = 7
    unique_chars = sorted([char for char in s])
    return unique_chars[:n][::-1]