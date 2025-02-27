def return_nth_smallest_ascii(string):
    chars_in_range = [char for char in string[17:84]]
    sorted_chars = sorted(chars_in_range)
    return sorted_chars[4]