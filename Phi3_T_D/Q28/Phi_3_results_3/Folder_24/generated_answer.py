def return_nth_smallest_ascii(input_string):
    target_range = input_string[34:82]
    return min(target_range, key=ord)