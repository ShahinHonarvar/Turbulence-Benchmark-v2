def return_nth_smallest_ascii(s):
    unique_chars = sorted(set(s[28:55]))
    return unique_chars[13] if len(unique_chars) > 13 else ''