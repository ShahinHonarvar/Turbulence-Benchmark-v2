def return_nth_smallest_ascii(s):
    target_chars = sorted(set(s[20:31]))
    if len(target_chars) < 8:
        return None
    return target_chars[7]