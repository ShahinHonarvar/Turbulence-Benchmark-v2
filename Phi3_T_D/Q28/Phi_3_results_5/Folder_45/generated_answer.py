def return_nth_smallest_ascii(s):
    unique_chars = sorted(set(s[0:16]))
    return unique_chars[15] if len(unique_chars) > 15 else unique_chars[-1]