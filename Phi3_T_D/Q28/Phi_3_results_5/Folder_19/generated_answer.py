def return_nth_smallest_ascii(input_string):
    sorted_chars = sorted(input_string[0:19])
    return sorted_chars[12] if len(sorted_chars) >= 13 else None