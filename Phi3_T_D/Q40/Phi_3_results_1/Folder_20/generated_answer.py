def return_n_smallest_chars(input_string):
    unique_chars = sorted(set(input_string))
    return unique_chars[:40]