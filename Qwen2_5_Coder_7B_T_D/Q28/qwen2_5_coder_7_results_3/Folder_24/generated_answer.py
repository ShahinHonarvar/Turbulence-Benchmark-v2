def return_nth_smallest_ascii(input_string):
    sliced_string = input_string[34:82]
    sorted_chars = sorted(set(sliced_string))
    return sorted_chars[11]