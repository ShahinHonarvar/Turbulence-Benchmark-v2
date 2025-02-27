def return_nth_smallest_ascii(s):
    target_chars = sorted(set(s[14:55]))
    return target_chars[10] if len(target_chars) >= 11 else None