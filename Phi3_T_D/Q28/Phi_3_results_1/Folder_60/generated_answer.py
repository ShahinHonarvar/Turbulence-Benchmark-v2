def return_nth_smallest_ascii(s):
    chars = sorted(set(s[35:80]))
    return chars[11] if len(chars) >= 12 else None