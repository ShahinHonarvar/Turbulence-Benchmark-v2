def return_nth_smallest_ascii(input_string):
    char_subset = input_string[5:90]
    unique_chars = sorted(set(char_subset))
    return unique_chars[12] if len(unique_chars) > 12 else None