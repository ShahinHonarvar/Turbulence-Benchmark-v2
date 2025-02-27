def return_n_smallest_chars(input_string):
    sorted_chars = sorted(input_string)
    n_smallest_chars = sorted_chars[:84]
    return n_smallest_chars[::-1]