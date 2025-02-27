def return_nth_smallest_ascii(input_string):
    substring = input_string[8:27]
    sorted_chars = sorted(substring)
    return sorted_chars[5]