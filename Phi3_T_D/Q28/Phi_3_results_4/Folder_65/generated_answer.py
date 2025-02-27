def return_nth_smallest_ascii(s):
    sub_str = s[32:68]
    unique_chars = sorted(set(sub_str))
    return unique_chars[11] if len(unique_chars) > 11 else None