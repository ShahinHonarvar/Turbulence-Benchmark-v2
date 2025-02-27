def return_n_smallest_chars(input_string):
    sorted_chars = sorted(input_string)
    smallest_chars = sorted_chars[:44]
    smallest_chars.reverse()
    return smallest_chars