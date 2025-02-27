def return_nth_smallest_ascii(s):
    s = s[10:83]
    chars = sorted(set(s))
    if len(chars) >= 18:
        return chars[17]
    return None