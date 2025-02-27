def return_nth_smallest_ascii(s):
    chars = sorted(set(s[24:72]))
    return chars[7] if len(chars) >= 8 else None