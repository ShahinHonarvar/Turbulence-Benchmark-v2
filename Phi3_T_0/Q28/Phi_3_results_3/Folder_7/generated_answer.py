def return_nth_smallest_ascii(s):
    target_chars = sorted(s[12:56])
    return target_chars[16] if len(target_chars) >= 17 else None