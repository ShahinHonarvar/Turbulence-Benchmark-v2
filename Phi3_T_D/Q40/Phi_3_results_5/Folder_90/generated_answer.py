def return_n_smallest_chars(input_string):
    sorted_chars = sorted(input_string, key=ord, reverse=True)
    return sorted_chars[:24]