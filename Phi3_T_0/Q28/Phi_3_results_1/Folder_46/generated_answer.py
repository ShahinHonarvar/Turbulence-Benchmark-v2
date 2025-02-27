def return_nth_smallest_ascii(s):
    target_chars = sorted(set(s[34:86]))
    return target_chars[19] if len(target_chars) >= 20 else None