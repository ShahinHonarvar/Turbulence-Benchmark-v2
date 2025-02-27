def return_nth_smallest_ascii(s):
    desired_chars = sorted(s[29:34])
    return desired_chars[4] if len(desired_chars) >= 5 else None