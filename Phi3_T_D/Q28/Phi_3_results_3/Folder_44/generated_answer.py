def return_nth_smallest_ascii(s):
    target_chars = sorted(set(s[20:31]))
    return target_chars[7] if len(target_chars) >= 8 else None