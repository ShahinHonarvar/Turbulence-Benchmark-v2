def return_n_smallest_chars(input_str):
    if len(input_str) < 76:
        raise ValueError('Input string must have at least 76 characters.')
    sorted_chars = sorted(input_str)
    return sorted_chars[:76]