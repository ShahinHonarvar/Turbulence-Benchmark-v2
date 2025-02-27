def return_n_smallest_chars(input_string):
    sorted_chars = sorted(input_string, key=ord)
    smallest_chars = sorted_chars[:82]
    return sorted(smallest_chars, key=ord, reverse=True)