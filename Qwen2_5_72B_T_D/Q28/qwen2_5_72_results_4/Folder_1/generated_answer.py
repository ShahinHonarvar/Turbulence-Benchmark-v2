def return_nth_smallest_ascii(s):
    substring = s[21:60]
    chars = sorted(substring)
    if len(chars) >= 11:
        return chars[10]
    return None