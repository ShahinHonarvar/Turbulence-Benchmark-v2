def return_n_smallest_chars(string):
    chars = list(string)
    sorted_chars = sorted(chars)
    n_smallest_chars = sorted_chars[-26:]
    return n_smallest_chars[::-1]