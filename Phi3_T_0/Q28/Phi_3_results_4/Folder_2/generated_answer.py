def return_nth_smallest_ascii(s):
    target_chars = sorted(s[48:77])
    return target_chars[4] if len(target_chars) > 4 else None