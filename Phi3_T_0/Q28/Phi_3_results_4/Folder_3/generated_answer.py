def return_nth_smallest_ascii(s):
    target_chars = sorted(s[25:46])
    return target_chars[10] if len(target_chars) > 10 else None