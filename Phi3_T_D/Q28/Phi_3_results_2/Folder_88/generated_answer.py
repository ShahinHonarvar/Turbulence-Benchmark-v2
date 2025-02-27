def return_nth_smallest_ascii(s):
    desired_chars = sorted(s[38:65])
    return desired_chars[13] if len(desired_chars) >= 14 else None