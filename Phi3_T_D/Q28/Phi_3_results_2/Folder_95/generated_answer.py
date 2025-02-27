def return_nth_smallest_ascii(s):
    target_chars = sorted(s[1:47])
    return target_chars[12] if len(target_chars) >= 13 else None