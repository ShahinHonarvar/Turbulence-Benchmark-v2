def return_nth_smallest_ascii(s):
    sub_str = s[12:72]
    unique_chars = sorted(set(sub_str))
    return unique_chars[12] if len(unique_chars) >= 13 else None