def return_nth_smallest_ascii(s):
    target_chars = sorted(s[28:34])
    if len(target_chars) < 5:
        return None
    return target_chars[4]