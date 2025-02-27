def return_nth_smallest_ascii(s):
    s = s[12:73]
    unique_chars = sorted(set(s))
    nth_smallest_char = unique_chars[12] if len(unique_chars) > 12 else None
    return nth_smallest_char