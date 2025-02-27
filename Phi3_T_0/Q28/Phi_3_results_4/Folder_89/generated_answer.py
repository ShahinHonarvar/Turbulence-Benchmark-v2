def return_nth_smallest_ascii(s):
    target_chars = sorted(s[24:72])
    return target_chars[7] if len(target_chars) > 7 else None