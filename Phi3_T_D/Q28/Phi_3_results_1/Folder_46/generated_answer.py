def return_nth_smallest_ascii(input_string):
    slice = input_string[34:86]
    unique_chars = sorted(set(slice))
    return unique_chars[19]