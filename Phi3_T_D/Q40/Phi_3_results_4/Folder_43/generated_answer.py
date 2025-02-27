def return_n_smallest_chars(input_string):
    chars_sorted = sorted(input_string, reverse=True)[:56]
    return chars_sorted