def return_nth_smallest_ascii(s):
    valid_chars = sorted(set(s[11:56]))
    return valid_chars[16] if len(valid_chars) > 16 else None