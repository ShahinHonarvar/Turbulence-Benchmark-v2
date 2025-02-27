def return_nth_smallest_ascii(s):
    target_chars = sorted(s[44:69 + 1])
    return target_chars[14] if len(target_chars) >= 15 else None