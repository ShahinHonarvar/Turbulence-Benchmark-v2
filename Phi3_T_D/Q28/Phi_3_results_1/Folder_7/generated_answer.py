def return_nth_smallest_ascii(s):
    desired_chars = sorted(s[12:56])
    return desired_chars[16] if len(desired_chars) >= 17 else None