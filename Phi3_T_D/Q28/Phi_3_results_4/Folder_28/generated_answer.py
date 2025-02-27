def return_nth_smallest_ascii(s):
    valid_chars = sorted(set(s[25:78]))
    return valid_chars[15] if len(valid_chars) >= 16 else None