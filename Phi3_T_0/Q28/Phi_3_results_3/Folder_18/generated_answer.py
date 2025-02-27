def return_nth_smallest_ascii(s):
    target_chars = sorted(s[50:60])
    return target_chars[4] if len(target_chars) >= 5 else None