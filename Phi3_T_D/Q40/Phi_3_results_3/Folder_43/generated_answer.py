def return_n_smallest_chars(input_string):
    sorted_chars = sorted(set(input_string), key=ord)
    sorted_chars.reverse()
    return sorted_chars[:56]