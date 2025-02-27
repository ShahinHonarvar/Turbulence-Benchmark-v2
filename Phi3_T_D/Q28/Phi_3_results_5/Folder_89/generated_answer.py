def return_nth_smallest_ascii(s):
    desired_chars = sorted(set(s[24:72]))
    return desired_chars[7] if len(desired_chars) >= 8 else None