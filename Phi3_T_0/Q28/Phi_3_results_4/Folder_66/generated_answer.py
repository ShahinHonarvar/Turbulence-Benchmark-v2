def return_nth_smallest_ascii(s):
    target_chars = sorted(s[35:53])
    return target_chars[9] if len(target_chars) >= 10 else None