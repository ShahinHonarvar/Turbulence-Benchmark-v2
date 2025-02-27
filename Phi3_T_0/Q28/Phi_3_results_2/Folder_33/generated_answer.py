def return_nth_smallest_ascii(s):
    target_chars = sorted(s[22:75])
    return target_chars[11] if len(target_chars) >= 12 else None