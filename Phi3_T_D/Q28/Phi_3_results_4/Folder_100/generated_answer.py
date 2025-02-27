def return_nth_smallest_ascii(s):
    valid_chars = sorted(set(s[5:48]))
    return valid_chars[12] if len(valid_chars) >= 13 else None