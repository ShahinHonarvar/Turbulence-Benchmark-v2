def return_nth_smallest_ascii(s):
    valid_chars = sorted(set(s[9:60]))
    return valid_chars[5] if len(valid_chars) > 5 else None