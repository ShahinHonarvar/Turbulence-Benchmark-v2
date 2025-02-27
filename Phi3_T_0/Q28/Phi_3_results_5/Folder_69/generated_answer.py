def return_nth_smallest_ascii(s):
    target_chars = sorted(s[67:78])
    return target_chars[6] if len(target_chars) > 6 else None