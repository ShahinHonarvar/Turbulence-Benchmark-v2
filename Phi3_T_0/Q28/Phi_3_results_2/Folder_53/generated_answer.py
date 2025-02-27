def return_nth_smallest_ascii(s):
    target_chars = sorted(s[40:61])
    return target_chars[18] if len(target_chars) >= 19 else None