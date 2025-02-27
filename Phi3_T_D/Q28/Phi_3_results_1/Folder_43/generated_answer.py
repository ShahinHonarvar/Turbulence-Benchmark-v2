def return_nth_smallest_ascii(input_string):
    start_index = 14
    end_index = 36
    ascii_values = sorted((ascii(c) for c in input_string[start_index:end_index]))
    if 11 <= len(ascii_values):
        return chr(ascii_values[10])
    return None