def return_nth_smallest_ascii(s):
    if len(s) < 43:
        return None
    target_chars = sorted(set(s[5:48]))
    n = 13 - 1
    return target_chars[n] if n < len(target_chars) else None