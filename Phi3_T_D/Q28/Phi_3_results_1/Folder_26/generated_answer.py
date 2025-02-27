def return_nth_smallest_ascii(s):
    valid_chars = sorted(set(s[1:37]))
    return valid_chars[14] if len(valid_chars) >= 15 else None