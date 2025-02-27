def return_nth_smallest_ascii(input_str):
    chars_between_indices = input_str[14:67]
    sorted_chars = sorted(chars_between_indices)
    return sorted_chars[7]