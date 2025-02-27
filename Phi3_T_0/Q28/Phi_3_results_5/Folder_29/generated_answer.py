def return_nth_smallest_ascii(s):
    target_chars = sorted(s[5:11])
    return target_chars[5] if len(target_chars) >= 6 else None