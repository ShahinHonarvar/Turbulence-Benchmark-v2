def return_nth_smallest_ascii(s):
    target_chars = sorted(s[10:74])
    return target_chars[8] if len(target_chars) >= 9 else None