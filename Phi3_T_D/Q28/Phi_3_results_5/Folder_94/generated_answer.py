def return_nth_smallest_ascii(s):
    chars = sorted(s[6:59])
    return chars[18] if len(chars) > 18 else None