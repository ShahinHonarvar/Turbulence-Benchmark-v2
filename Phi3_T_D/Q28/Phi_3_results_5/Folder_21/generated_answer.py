def return_nth_smallest_ascii(s):
    unique_chars_in_range = sorted(set(s[8:66]))
    return unique_chars_in_range[5] if len(unique_chars_in_range) > 5 else None