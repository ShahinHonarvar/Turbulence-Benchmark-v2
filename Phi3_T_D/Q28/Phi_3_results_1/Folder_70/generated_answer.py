def return_nth_smallest_ascii(s):
    target_chars = sorted(s[28:55])
    if len(target_chars) < 14:
        return None
    return target_chars[13]