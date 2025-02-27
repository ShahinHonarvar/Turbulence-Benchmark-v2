def return_nth_smallest_ascii(s):
    target_chars = sorted(s[34:82])
    return target_chars[11] if len(target_chars) >= 12 else None