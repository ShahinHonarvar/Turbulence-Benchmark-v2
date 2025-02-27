def return_nth_smallest_ascii(s):
    target_chars = sorted(set(s[47:81]))
    return target_chars[3] if len(target_chars) > 3 else None