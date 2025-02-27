def return_nth_smallest_ascii(s):
    target_chars = sorted(s[52:80])
    return target_chars[6] if len(target_chars) >= 7 else None