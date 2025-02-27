def return_nth_smallest_ascii(string):
    start_index, end_index = (17, 83)
    chars_in_range = string[start_index:end_index + 1]
    return sorted(set(chars_in_range))[4]